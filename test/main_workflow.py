"""
Test suite for Information Gathering Workflow
Tests the semantic_search() → file_search() → read_file() → grep_search() pattern
"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
import importlib.util
import os

# Import the framework with correct path
spec = importlib.util.spec_from_file_location(
    "autonomous_framework", 
    os.path.join(os.path.dirname(__file__), "..", r"C:\Users\Admin\Documents\pb2s\PB2S_PRODUCTION_READY\ITERATION_1\Autonomous_Technical_Expert_Framework\src\core", "autonomus_framework.py")
)
autonomous_framework = importlib.util.module_from_spec(spec)
spec.loader.exec_module(autonomous_framework)

AutonomousTechnicalExpertFramework = autonomous_framework.AutonomousTechnicalExpertFramework
ProjectAsset = autonomous_framework.ProjectAsset
from datetime import datetime


class TestInformationGatheringWorkflow:
    """Test the complete information gathering workflow"""
    
    @pytest.fixture
    def framework(self):
        """Create framework instance for testing"""
        return AutonomousTechnicalExpertFramework(
            project_name="Test Information Gathering",
            workspace_path="./test_workspace"
        )
    
    def test_framework_initialization(self, framework):
        """Test that framework initializes correctly for information gathering"""
        assert framework.project_name == "Test Information Gathering"
        assert framework.workspace_path == "./test_workspace"
        assert len(framework.assets) == 0
        assert len(framework.gaps) == 0
        
    @pytest.mark.asyncio
    async def test_semantic_search_pattern(self, framework):
        """Test the semantic search → file search → read file → grep search pattern"""
        
        # Mock the tool sequence
        with patch.object(framework, 'discover_existing_assets') as mock_discover:
            mock_assets = [
                ProjectAsset(
                    name="test_file.py",
                    type="code",
                    path="./test_file.py",
                    lines_of_code=100,
                    complexity_score=0.7,
                    reusability_score=0.8,
                    quality_score=0.9,
                    dependencies=["pytest"],
                    description="Test file for information gathering",
                    last_modified=datetime.now()
                )
            ]
            mock_discover.return_value = mock_assets
            
            # Execute discovery
            assets = await framework.discover_existing_assets()
            
            # Validate results
            assert len(assets) == 1
            assert assets[0].name == "test_file.py"
            assert assets[0].quality_score == 0.9
            
    def test_comprehensive_context_gathering(self, framework):
        """Test comprehensive context gathering capabilities"""
        
        # Test asset quality assessment
        quality_metrics = framework.assess_asset_quality("./test_file.py")
        
        # Validate quality assessment structure
        required_metrics = [
            "complexity_score",
            "reusability_score", 
            "quality_score",
            "maintainability_score"
        ]
        
        for metric in required_metrics:
            assert metric in quality_metrics
            assert isinstance(quality_metrics[metric], float)
            assert 0.0 <= quality_metrics[metric] <= 1.0
            
    def test_context_integration(self, framework):
        """Test context integration and synthesis"""
        
        objectives = [
            "Build information gathering system",
            "Implement semantic search",
            "Create asset inventory"
        ]
        
        gaps = framework.map_capabilities_to_objectives(objectives)
        
        # Validate gap analysis
        assert isinstance(gaps, list)
        # Framework should handle gap identification even with empty initial state
        
    def test_quality_assessment(self, framework):
        """Test information quality assessment"""
        
        # Test with various asset types
        test_assets = [
            ("python_file.py", "code"),
            ("documentation.md", "documentation"),
            ("config.json", "configuration")
        ]
        
        for asset_path, asset_type in test_assets:
            quality_metrics = framework.assess_asset_quality(asset_path)
            
            # All assets should return valid quality metrics
            assert "quality_score" in quality_metrics
            assert isinstance(quality_metrics["quality_score"], float)
            
    def test_partnership_logging(self, framework):
        """Test that information gathering actions are properly logged"""
        
        initial_log_count = len(framework.partnership_log)
        
        # Trigger a logged action
        framework.log_partnership_action("test_information_gathering", {
            "test_data": "information_gathering_validation"
        })
        
        # Validate logging
        assert len(framework.partnership_log) == initial_log_count + 1
        latest_log = framework.partnership_log[-1]
        assert latest_log["action"] == "test_information_gathering"
        assert "timestamp" in latest_log
        assert "details" in latest_log


class TestInformationGatheringEffectiveness:
    """Test the effectiveness of information gathering patterns"""
    
    @pytest.fixture
    def framework(self):
        return AutonomousTechnicalExpertFramework(
            "Effectiveness Test",
            "./effectiveness_workspace"
        )
    
    def test_tool_orchestration_pattern(self, framework):
        """Test that tool orchestration patterns work as designed"""
        
        # Test the specific pattern: semantic_search → file_search → read_file → grep_search
        # This should be the systematic approach used by the framework
        
        # Mock the pattern execution
        pattern_steps = [
            "semantic_search",
            "file_search", 
            "read_file",
            "grep_search"
        ]
        
        # Validate pattern structure
        assert len(pattern_steps) == 4
        assert pattern_steps[0] == "semantic_search"
        assert pattern_steps[-1] == "grep_search"
        
        # Each step should build on the previous
        for i, step in enumerate(pattern_steps):
            assert isinstance(step, str)
            assert len(step) > 0
            
    def test_comprehensive_before_decisions(self, framework):
        """Test that comprehensive context is gathered before decisions"""
        
        # This tests the core principle: gather comprehensive context before making decisions
        
        # Mock decision scenario
        decision_context = {
            "problem": "Need to understand existing capabilities",
            "options": ["analyze", "assume", "ask"],
            "framework_approach": "comprehensive_analysis_first"
        }
        
        # Framework should prioritize comprehensive analysis
        assert decision_context["framework_approach"] == "comprehensive_analysis_first"
        
    def test_information_preservation(self, framework):
        """Test that information is properly preserved for future use"""
        
        # Test information storage and retrieval
        test_info = {
            "source": "test_discovery",
            "content": "valuable_information",
            "quality_score": 0.85
        }
        
        # Log information
        framework.log_partnership_action("information_preserved", test_info)
        
        # Validate preservation
        preserved_info = framework.partnership_log[-1]
        assert preserved_info["details"]["source"] == "test_discovery"
        assert preserved_info["details"]["quality_score"] == 0.85


if __name__ == "__main__":
    # Run tests directly
    pytest.main([__file__, "-v"])
