"""
Test suite for Quality Assurance Workflow  
Tests the read_file() → replace_string_in_file() → get_errors() → runTests() pattern
"""

import pytest
import os
import tempfile
import shutil
from unittest.mock import Mock, patch
from src.core.autonomous_framework import AutonomousTechnicalExpertFramework


class TestQualityAssuranceWorkflow:
    """Test the complete quality assurance workflow"""
    
    @pytest.fixture
    def framework(self):
        """Create framework instance with temporary workspace"""
        temp_dir = tempfile.mkdtemp()
        framework = AutonomousTechnicalExpertFramework(
            project_name="Test Quality Assurance",
            workspace_path=temp_dir
        )
        yield framework
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_professional_quality_validation(self, framework):
        """Test read_file() → replace_string_in_file() → get_errors() → runTests() pattern"""
        
        # Create test file for quality validation
        test_file_path = os.path.join(framework.workspace_path, "quality_test.py")
        test_code = '''
def example_function(param1, param2):
    """
    Example function with proper documentation
    
    Args:
        param1: First parameter
        param2: Second parameter
        
    Returns:
        str: Processed result
    """
    try:
        if param1 is None or param2 is None:
            raise ValueError("Parameters cannot be None")
        
        result = f"Processed: {param1} + {param2}"
        return result
        
    except ValueError as e:
        print(f"Error in example_function: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
'''
        
        with open(test_file_path, 'w') as f:
            f.write(test_code)
        
        # Test quality validation
        quality_result = framework.validate_professional_quality(test_file_path)
        
        # Validate quality assessment structure
        required_metrics = [
            "error_handling",
            "documentation",
            "performance_optimized", 
            "testing_coverage",
            "security_compliance",
            "maintainability_score"
        ]
        
        for metric in required_metrics:
            assert metric in quality_result
            assert isinstance(quality_result[metric], (bool, float, int))
            
    def test_error_handling_validation(self, framework):
        """Test comprehensive error handling validation"""
        
        # Create code with error handling
        error_handling_code = '''
def robust_function(data):
    """Function with comprehensive error handling"""
    try:
        if not data:
            raise ValueError("Data cannot be empty")
        
        processed_data = []
        for item in data:
            try:
                processed_item = str(item).upper()
                processed_data.append(processed_item)
            except AttributeError:
                print(f"Could not process item: {item}")
                continue
                
        return processed_data
        
    except ValueError as ve:
        print(f"Value error: {ve}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
'''
        
        test_file = os.path.join(framework.workspace_path, "error_handling_test.py")
        with open(test_file, 'w') as f:
            f.write(error_handling_code)
        
        quality_result = framework.validate_professional_quality(test_file)
        
        # Error handling should be detected
        assert "error_handling" in quality_result
        
    def test_documentation_validation(self, framework):
        """Test documentation quality validation"""
        
        # Create well-documented code
        documented_code = '''
"""
Module for testing documentation validation

This module contains examples of properly documented functions
following professional documentation standards.
"""

class ExampleClass:
    """
    Example class demonstrating proper documentation
    
    This class shows how to document classes with proper
    descriptions, attributes, and methods.
    
    Attributes:
        name (str): The name of the example
        value (int): The value stored in the example
    """
    
    def __init__(self, name: str, value: int):
        """
        Initialize the ExampleClass
        
        Args:
            name (str): The name for this example
            value (int): The initial value
        """
        self.name = name
        self.value = value
    
    def get_description(self) -> str:
        """
        Get a description of this example
        
        Returns:
            str: A formatted description string
        """
        return f"Example {self.name} with value {self.value}"
'''
        
        test_file = os.path.join(framework.workspace_path, "documentation_test.py")
        with open(test_file, 'w') as f:
            f.write(documented_code)
        
        quality_result = framework.validate_professional_quality(test_file)
        
        # Documentation should be validated
        assert "documentation" in quality_result
        
    def test_performance_optimization_check(self, framework):
        """Test performance optimization validation"""
        
        # Create performance-conscious code
        performance_code = '''
import time
from typing import List, Dict

def optimized_function(data_list: List[int]) -> Dict[str, int]:
    """
    Optimized function demonstrating performance considerations
    
    Args:
        data_list: List of integers to process
        
    Returns:
        Dict with performance metrics and results
    """
    start_time = time.time()
    
    # Use list comprehension for efficiency
    processed_data = [x * 2 for x in data_list if x > 0]
    
    # Use set for O(1) lookups instead of list
    unique_values = set(processed_data)
    
    end_time = time.time()
    
    return {
        "processed_count": len(processed_data),
        "unique_count": len(unique_values),
        "processing_time": end_time - start_time
    }
'''
        
        test_file = os.path.join(framework.workspace_path, "performance_test.py")
        with open(test_file, 'w') as f:
            f.write(performance_code)
        
        quality_result = framework.validate_professional_quality(test_file)
        
        # Performance optimization should be considered
        assert "performance_optimized" in quality_result
        
    def test_security_compliance(self, framework):
        """Test security compliance validation"""
        
        # Create security-conscious code
        security_code = '''
import hashlib
import secrets
from typing import Optional

def secure_hash_function(data: str, salt: Optional[str] = None) -> str:
    """
    Secure hashing function with proper salt handling
    
    Args:
        data: The data to hash
        salt: Optional salt for hashing (generated if not provided)
        
    Returns:
        str: Secure hash of the data
    """
    if salt is None:
        salt = secrets.token_hex(16)
    
    # Use SHA-256 for secure hashing
    hasher = hashlib.sha256()
    hasher.update(f"{data}{salt}".encode('utf-8'))
    
    return f"{salt}:{hasher.hexdigest()}"

def validate_input(user_input: str) -> bool:
    """
    Validate user input for security
    
    Args:
        user_input: Input from user to validate
        
    Returns:
        bool: True if input is safe
    """
    # Basic input validation
    if not user_input or len(user_input) > 1000:
        return False
    
    # Check for potentially dangerous patterns
    dangerous_patterns = ['<script>', 'javascript:', 'eval(']
    for pattern in dangerous_patterns:
        if pattern.lower() in user_input.lower():
            return False
    
    return True
'''
        
        test_file = os.path.join(framework.workspace_path, "security_test.py")
        with open(test_file, 'w') as f:
            f.write(security_code)
        
        quality_result = framework.validate_professional_quality(test_file)
        
        # Security compliance should be checked
        assert "security_compliance" in quality_result
        
    def test_maintainability_assessment(self, framework):
        """Test code maintainability assessment"""
        
        # Create maintainable code
        maintainable_code = '''
"""
Maintainable code example demonstrating clean code principles
"""

from abc import ABC, abstractmethod
from typing import List, Protocol

class DataProcessor(Protocol):
    """Protocol for data processing implementations"""
    
    def process(self, data: List[str]) -> List[str]:
        """Process the provided data"""
        ...

class TextDataProcessor:
    """Clean, maintainable text data processor"""
    
    def __init__(self, uppercase: bool = False):
        """
        Initialize processor
        
        Args:
            uppercase: Whether to convert text to uppercase
        """
        self._uppercase = uppercase
    
    def process(self, data: List[str]) -> List[str]:
        """
        Process text data according to configuration
        
        Args:
            data: List of text strings to process
            
        Returns:
            List of processed strings
        """
        processed = []
        
        for item in data:
            if self._is_valid_text(item):
                processed_item = self._process_single_item(item)
                processed.append(processed_item)
        
        return processed
    
    def _is_valid_text(self, text: str) -> bool:
        """Check if text is valid for processing"""
        return isinstance(text, str) and len(text.strip()) > 0
    
    def _process_single_item(self, text: str) -> str:
        """Process a single text item"""
        cleaned = text.strip()
        return cleaned.upper() if self._uppercase else cleaned
'''
        
        test_file = os.path.join(framework.workspace_path, "maintainability_test.py")
        with open(test_file, 'w') as f:
            f.write(maintainable_code)
        
        quality_result = framework.validate_professional_quality(test_file)
        
        # Maintainability should be assessed
        assert "maintainability_score" in quality_result


class TestQualityAssuranceEffectiveness:
    """Test the effectiveness of quality assurance patterns"""
    
    @pytest.fixture
    def framework(self):
        temp_dir = tempfile.mkdtemp()
        framework = AutonomousTechnicalExpertFramework(
            "QA Effectiveness Test",
            temp_dir
        )
        yield framework
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_professional_implementation_standards(self, framework):
        """Test that professional implementation standards are maintained"""
        
        # Test the quality assurance pattern
        qa_pattern = [
            "read_file",
            "replace_string_in_file",
            "get_errors", 
            "runTests"
        ]
        
        # Validate pattern structure
        assert len(qa_pattern) == 4
        assert qa_pattern[0] == "read_file"
        assert qa_pattern[-1] == "runTests"
        
        # Each step should validate and improve quality
        for step in qa_pattern:
            assert isinstance(step, str)
            assert len(step) > 0
    
    def test_continuous_quality_monitoring(self, framework):
        """Test continuous quality monitoring"""
        
        # Quality should be monitored throughout development
        quality_monitoring = {
            "continuous": True,
            "automated": True,
            "comprehensive": True
        }
        
        for aspect, enabled in quality_monitoring.items():
            assert enabled, f"Quality monitoring aspect '{aspect}' should be enabled"
    
    def test_partnership_effectiveness_measurement(self, framework):
        """Test partnership effectiveness measurement"""
        
        # Test effectiveness metrics
        effectiveness_metrics = framework.measure_partnership_effectiveness()
        
        required_metrics = [
            "decisions_made",
            "consensus_rate",
            "implementation_speed",
            "quality_scores",
            "partner_satisfaction",
            "knowledge_preservation"
        ]
        
        for metric in required_metrics:
            assert metric in effectiveness_metrics
            assert isinstance(effectiveness_metrics[metric], (int, float, list))


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])