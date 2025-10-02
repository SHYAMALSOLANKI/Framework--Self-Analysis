"""
Cognitive Architecture Validation Script
Validates the cognitive patterns and decision-making architecture of the framework
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.core.autonomous_framework import AutonomousTechnicalExpertFramework


def validate_cognitive_architecture():
    """Validate cognitive architecture and decision-making patterns"""
    
    print("=" * 60)
    print("COGNITIVE ARCHITECTURE VALIDATION")
    print("=" * 60)
    
    # Create a temporary framework instance
    framework = AutonomousTechnicalExpertFramework(
        project_name="Cognitive Validation",
        workspace_path="/tmp/cognitive_test"
    )
    
    validation_results = []
    
    print("\n🧠 VALIDATING COGNITIVE PATTERNS:")
    print("-" * 60)
    
    # Test 1: Information Gathering Pattern
    print("\n1. Information Gathering Capability...")
    try:
        info_result = framework.gather_comprehensive_information("test query")
        has_context = "context_files" in info_result
        has_requirements = "requirements" in info_result
        has_architecture = "architecture_info" in info_result
        
        ig_valid = has_context and has_requirements and has_architecture
        validation_results.append(("Information Gathering", ig_valid))
        print(f"   ✓ Information gathering pattern validated: {ig_valid}")
    except Exception as e:
        validation_results.append(("Information Gathering", False))
        print(f"   ✗ Information gathering failed: {e}")
    
    # Test 2: Partnership Decision Making
    print("\n2. Partnership Decision Making...")
    try:
        decision_result = framework.make_partnership_decision({
            "phase": "test",
            "decision": "test decision",
            "ai_recommendation": "option A",
            "human_input": "option B"
        })
        
        pdm_valid = decision_result.get("consensus_reached", False)
        validation_results.append(("Partnership Decision Making", pdm_valid))
        print(f"   ✓ Partnership decision making validated: {pdm_valid}")
    except Exception as e:
        validation_results.append(("Partnership Decision Making", False))
        print(f"   ✗ Partnership decision making failed: {e}")
    
    # Test 3: Knowledge Preservation
    print("\n3. Knowledge Preservation...")
    try:
        test_knowledge = {"test_key": "test_value", "learning": "test learning"}
        framework.preserve_knowledge(test_knowledge)
        preserved = framework.get_preserved_knowledge()
        
        kp_valid = "test_key" in preserved and preserved["test_key"] == "test_value"
        validation_results.append(("Knowledge Preservation", kp_valid))
        print(f"   ✓ Knowledge preservation validated: {kp_valid}")
    except Exception as e:
        validation_results.append(("Knowledge Preservation", False))
        print(f"   ✗ Knowledge preservation failed: {e}")
    
    # Test 4: Continuous Improvement
    print("\n4. Continuous Improvement Cycle...")
    try:
        cycle_result = framework.run_complete_cycle("test task", [])
        
        ci_valid = "effectiveness_score" in cycle_result
        validation_results.append(("Continuous Improvement", ci_valid))
        print(f"   ✓ Continuous improvement cycle validated: {ci_valid}")
    except Exception as e:
        validation_results.append(("Continuous Improvement", False))
        print(f"   ✗ Continuous improvement failed: {e}")
    
    # Test 5: Error Handling
    print("\n5. Error Handling & Recovery...")
    try:
        error_result = framework.handle_system_error(
            Exception("test error"), "test scenario"
        )
        
        eh_valid = error_result.get("error_handled", False)
        validation_results.append(("Error Handling", eh_valid))
        print(f"   ✓ Error handling validated: {eh_valid}")
    except Exception as e:
        validation_results.append(("Error Handling", False))
        print(f"   ✗ Error handling failed: {e}")
    
    # Test 6: Professional Standards
    print("\n6. Professional Standards Compliance...")
    try:
        standards = framework.validate_professional_standards()
        
        ps_valid = standards.get("standards_met", False)
        validation_results.append(("Professional Standards", ps_valid))
        print(f"   ✓ Professional standards validated: {ps_valid}")
    except Exception as e:
        validation_results.append(("Professional Standards", False))
        print(f"   ✗ Professional standards failed: {e}")
    
    # Test 7: Autonomous Operation
    print("\n7. Autonomous Operation Capability...")
    try:
        auto_result = framework.run_autonomous_cycle("test task", 1)
        
        ao_valid = auto_result.get("autonomous_execution", False)
        validation_results.append(("Autonomous Operation", ao_valid))
        print(f"   ✓ Autonomous operation validated: {ao_valid}")
    except Exception as e:
        validation_results.append(("Autonomous Operation", False))
        print(f"   ✗ Autonomous operation failed: {e}")
    
    # Summary
    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY:")
    print("-" * 60)
    
    passed = sum(1 for _, valid in validation_results if valid)
    total = len(validation_results)
    success_rate = passed / total if total > 0 else 0
    
    for component, valid in validation_results:
        status = "✅ PASS" if valid else "❌ FAIL"
        print(f"  {component:.<45} {status}")
    
    print("-" * 60)
    print(f"  Results: {passed}/{total} tests passed ({success_rate:.1%})")
    print("=" * 60)
    
    if success_rate >= 0.85:
        print("\n🎉 COGNITIVE ARCHITECTURE VALIDATED SUCCESSFULLY!")
        return True
    else:
        print("\n⚠️  COGNITIVE ARCHITECTURE NEEDS IMPROVEMENT")
        return False


if __name__ == "__main__":
    try:
        result = validate_cognitive_architecture()
        sys.exit(0 if result else 1)
    except Exception as e:
        print(f"\n❌ Error validating cognitive architecture: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
