# NAAC Scoring Engine - Based on Dr. Radhakrishnan Committee Report
import streamlit as st
import pandas as pd
import numpy as np
from config.naac_config import (
    CRITERIA, TOTAL_WEIGHTAGE, BINARY_ACCREDITATION, 
    MATURITY_LEVELS, METRICS
)

class NAACScoringEngine:
    def __init__(self):
        self.criteria = CRITERIA
        self.total_weightage = TOTAL_WEIGHTAGE
        self.binary_accreditation = BINARY_ACCREDITATION
        self.maturity_levels = MATURITY_LEVELS
        self.metrics = METRICS
    
    def calculate_criterion_score(self, metric_responses, criterion_num):
        """Calculate score for a single criterion using IPOI framework"""
        criterion_metrics = {k: v for k, v in self.metrics.items() 
                            if k.startswith(f'{criterion_num}.')}
        
        total_weight = 0
        total_score = 0
        
        for metric_code, metric_data in criterion_metrics.items():
            weight = metric_data['weight']
            total_weight += weight
            
            response = metric_responses.get(metric_code, {}).get('response')
            score = self._score_metric(metric_code, response, metric_data['ipo'])
            total_score += (score * weight / 4)  # Normalize to 0-4 scale
        
        if total_weight > 0:
            return (total_score / total_weight) * 4  # Return on 0-4 scale
        return 0
    
    def _score_metric(self, metric_code, response, ipo_type):
        """Score individual metric based on IPOI framework"""
        if not response:
            return 0
        
        # Different scoring based on IPO type
        if ipo_type == "Input":
            return self._score_input_metric(response)
        elif ipo_type == "Process":
            return self._score_process_metric(response)
        elif ipo_type == "Outcome":
            return self._score_outcome_metric(response)
        elif ipo_type == "Impact":
            return self._score_impact_metric(response)
        return 2.0  # Default
    
    def _score_input_metric(self, response):
        """Score input metrics - completeness of documentation"""
        if isinstance(response, dict):
            completeness = sum(1 for v in response.values() if v) / max(1, len(response))
            return min(4.0, completeness * 4)
        elif isinstance(response, str) and response:
            return 3.0 if len(response) > 100 else 2.0
        elif response:
            return 3.0
        return 0
    
    def _score_process_metric(self, response):
        """Score process metrics - quality of implementation"""
        # Process quality scoring
        if isinstance(response, dict):
            if response.get('documents_uploaded'):
                return 3.5
        return 2.5
    
    def _score_outcome_metric(self, response):
        """Score outcome metrics - achievement levels"""
        if isinstance(response, dict):
            if 'percentage' in response:
                pct = response['percentage']
                if pct >= 90:
                    return 4.0
                elif pct >= 75:
                    return 3.0
                elif pct >= 60:
                    return 2.0
                elif pct >= 50:
                    return 1.0
                return 0
        return 2.0
    
    def _score_impact_metric(self, response):
        """Score impact metrics - long-term effects"""
        # Impact scoring - evidence of change
        if isinstance(response, dict):
            if response.get('has_evidence'):
                return 3.5
        return 2.0
    
    def calculate_all_criteria_scores(self, metric_responses):
        """Calculate scores for all 10 criteria"""
        scores = {}
        for criterion_num in range(1, 11):
            scores[criterion_num] = self.calculate_criterion_score(metric_responses, criterion_num)
        return scores
    
    def calculate_total_score(self, metric_responses):
        """Calculate total percentage score"""
        criterion_scores = self.calculate_all_criteria_scores(metric_responses)
        
        total_weighted_score = 0
        for criterion_num, score in criterion_scores.items():
            weight = self.criteria[criterion_num]['weight']
            total_weighted_score += (score / 4) * weight
        
        return (total_weighted_score / self.total_weightage) * 100
    
    def get_binary_accreditation(self, total_percentage):
        """Determine binary accreditation status"""
        for status, criteria in self.binary_accreditation.items():
            if total_percentage >= criteria.get('min_score', 0):
                if status == "accredited" and total_percentage >= criteria['min_score']:
                    return status
                elif status == "awaiting_accreditation":
                    if criteria.get('min_score', 0) <= total_percentage <= criteria.get('max_score', 100):
                        return status
                elif status == "not_accredited":
                    if total_percentage <= criteria.get('max_score', 49):
                        return status
        return "not_accredited"
    
    def get_maturity_level(self, total_percentage):
        """Determine maturity level for accredited institutions"""
        for level, criteria in self.maturity_levels.items():
            if total_percentage >= criteria['min_score']:
                return level
        return 1
    
    def get_ipo_breakdown(self, metric_responses, criterion_num):
        """Get IPOI breakdown for a criterion"""
        breakdown = {"Input": 0, "Process": 0, "Outcome": 0, "Impact": 0}
        weights = {"Input": 0, "Process": 0, "Outcome": 0, "Impact": 0}
        
        criterion_metrics = {k: v for k, v in self.metrics.items() 
                            if k.startswith(f'{criterion_num}.')}
        
        for metric_code, metric_data in criterion_metrics.items():
            ipo = metric_data['ipo']
            weight = metric_data['weight']
            weights[ipo] += weight
            
            response = metric_responses.get(metric_code, {}).get('response')
            score = self._score_metric(metric_code, response, ipo)
            breakdown[ipo] += (score / 4) * weight
        
        # Normalize
        for ipo in breakdown:
            if weights[ipo] > 0:
                breakdown[ipo] = (breakdown[ipo] / weights[ipo]) * 100
        
        return breakdown
    
    def generate_report(self, metric_responses, institution_data):
        """Generate comprehensive accreditation report"""
        total_percentage = self.calculate_total_score(metric_responses)
        binary_status = self.get_binary_accreditation(total_percentage)
        maturity_level = self.get_maturity_level(total_percentage) if binary_status == "accredited" else None
        criterion_scores = self.calculate_all_criteria_scores(metric_responses)
        
        # Generate IPOI breakdowns
        ipo_breakdowns = {}
        for criterion_num in range(1, 11):
            ipo_breakdowns[criterion_num] = self.get_ipo_breakdown(metric_responses, criterion_num)
        
        # Generate recommendations
        recommendations = []
        for criterion_num in range(1, 11):
            score = criterion_scores[criterion_num]
            if score < 2.0:
                recommendations.append(f"Criterion {criterion_num}: {self.criteria[criterion_num]['name']} needs improvement (Score: {score:.2f}/4.00)")
            elif score < 3.0:
                recommendations.append(f"Criterion {criterion_num}: {self.criteria[criterion_num]['name']} has room for improvement")
        
        return {
            'total_percentage': total_percentage,
            'binary_status': binary_status,
            'maturity_level': maturity_level,
            'criterion_scores': criterion_scores,
            'ipo_breakdowns': ipo_breakdowns,
            'recommendations': recommendations,
            'institution_category': institution_data.get('orientation_category', 'Not specified'),
            'legacy_category': institution_data.get('legacy_category', 'Not specified')
        }
    
    def get_progress_summary(self, metric_responses):
        """Get progress summary by criterion"""
        progress = []
        for criterion_num in range(1, 11):
            criterion_metrics = {k: v for k, v in self.metrics.items() 
                                if k.startswith(f'{criterion_num}.')}
            
            total = len(criterion_metrics)
            completed = sum(1 for code in criterion_metrics.keys() 
                          if code in metric_responses and metric_responses[code].get('response'))
            
            progress.append({
                'criterion': criterion_num,
                'name': self.criteria[criterion_num]['name'],
                'weight': self.criteria[criterion_num]['weight'],
                'total_metrics': total,
                'completed_metrics': completed,
                'percentage': (completed / total * 100) if total > 0 else 0
            })
        return progress
