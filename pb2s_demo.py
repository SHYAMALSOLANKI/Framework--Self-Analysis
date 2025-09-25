"""
PB2S Framework Integration Demonstration
Shows the JSON structures as requested in the problem statement
"""

import json
import os
import sys

# Import the framework
sys.path.insert(0, os.path.dirname(__file__))
import importlib.util
spec = importlib.util.spec_from_file_location(
    "autonomus_framework", 
    os.path.join(os.path.dirname(__file__), r"C:\Users\Admin\Documents\pb2s\PB2S_PRODUCTION_READY\ITERATION_1\Autonomous_Technical_Expert_Framework\src\core", "autonomus_framework.py")
)
autonomus_framework = importlib.util.module_from_spec(spec)
spec.loader.exec_module(autonomus_framework)

def demonstrate_pb2s_structures():
    """Demonstrate the PB2S JSON structures from the problem statement"""
    
    print("=== PB2S FRAMEWORK JSON STRUCTURES DEMONSTRATION ===\n")
    
    # Get the structures from the framework
    PB2SStructures = autonomus_framework.PB2SStructures
    FrameworkIntegration = autonomus_framework.FrameworkIntegration
    
    print("1. PB2S SINGLE CYCLE STRUCTURE:")
    print("=" * 50)
    single_cycle = PB2SStructures.get_single_cycle_structure()
    print(json.dumps(single_cycle, indent=2))
    
    print("\n\n2. PB2S COMPLETE 3-CYCLES STRUCTURE:")
    print("=" * 50)
    complete_cycles = PB2SStructures.get_complete_three_cycles_structure()
    print(json.dumps(complete_cycles, indent=2))
    
    print("\n\n3. VS CODE SNIPPETS FOR PB2S:")
    print("=" * 50)
    snippets = FrameworkIntegration.generate_pb2s_vscode_snippets()
    print(json.dumps(snippets, indent=2))
    
    print("\n\n4. FRAMEWORK INTEGRATION EXAMPLE:")
    print("=" * 50)
    
    # Create a framework instance and demonstrate PB2S integration
    framework = autonomus_framework.AutonomousTechnicalExpertFramework(
        project_name="PB2S Integration Demo",
        workspace_path="./demo_workspace"
    )
    
    # Create sample cycles
    framework.create_pb2s_cycle(
        cycle_number=1,
        perception_input="Project requirements analysis",
        analysis_results={
            "contradictions_found": False,
            "assumptions_found": True,
            "missing_evidence": True
        },
        reflection_flags=["assumption", "missing_evidence"],
        reflection_recommendation="Validate assumptions and gather missing evidence",
        action_taken="Scheduled stakeholder interviews"
    )
    
    framework.create_pb2s_cycle(
        cycle_number=2,
        perception_input="Stakeholder feedback received",
        analysis_results={
            "contradictions_found": True,
            "assumptions_found": False,
            "missing_evidence": False
        },
        reflection_flags=["contradiction"],
        reflection_recommendation="Resolve contradictions between stakeholders",
        action_taken="Organized alignment workshop"
    )
    
    framework.create_pb2s_cycle(
        cycle_number=3,
        perception_input="Aligned requirements and approach",
        analysis_results={
            "contradictions_found": False,
            "assumptions_found": False,
            "missing_evidence": False
        },
        reflection_flags=[],
        reflection_recommendation="All requirements are clear and validated",
        action_taken="Commenced implementation phase"
    )
    
    # Generate the populated PB2S structure
    populated_structure = framework.generate_pb2s_json_structure(single_cycle=False)
    print("POPULATED PB2S STRUCTURE WITH REAL DATA:")
    print(json.dumps(populated_structure, indent=2))
    
    # Validate conformance
    conformance = framework.validate_pb2s_conformance()
    print(f"\nPB2S CONFORMANCE VALIDATION:")
    print(f"- Conformant: {conformance['conformant']}")
    print(f"- Total Cycles: {conformance['total_cycles']}")
    print(f"- Mandatory Cycles Met: {conformance['mandatory_cycles_met']}")
    
    print("\n=== DEMONSTRATION COMPLETE ===")

if __name__ == "__main__":
    demonstrate_pb2s_structures()