"""
Framework Effectiveness Measurement Script
Measures and reports the effectiveness of the Autonomous Technical Expert Framework
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.core.autonomous_framework import AutonomousTechnicalExpertFramework


def measure_framework_effectiveness():
    """Measure and report framework effectiveness metrics"""
    
    print("=" * 60)
    print("FRAMEWORK EFFECTIVENESS MEASUREMENT")
    print("=" * 60)
    
    # Create a temporary framework instance
    framework = AutonomousTechnicalExpertFramework(
        project_name="Effectiveness Measurement",
        workspace_path="/tmp/effectiveness_test"
    )
    
    # Measure effectiveness
    effectiveness = framework.measure_framework_effectiveness()
    
    print("\n📊 EFFECTIVENESS METRICS:")
    print("-" * 60)
    
    for metric, value in effectiveness.items():
        if isinstance(value, float):
            print(f"  {metric:.<50} {value:.2%}")
        else:
            print(f"  {metric:.<50} {value}")
    
    print("\n" + "=" * 60)
    
    # Calculate overall score
    overall_score = effectiveness.get("overall_framework_score", 0.0)
    
    if overall_score > 0.9:
        status = "EXCELLENT ✅"
    elif overall_score > 0.75:
        status = "GOOD ✓"
    elif overall_score > 0.6:
        status = "SATISFACTORY ~"
    else:
        status = "NEEDS IMPROVEMENT ✗"
    
    print(f"\n🎯 OVERALL FRAMEWORK STATUS: {status}")
    print(f"   Framework Score: {overall_score:.2%}")
    print("\n" + "=" * 60)
    
    return effectiveness


if __name__ == "__main__":
    try:
        results = measure_framework_effectiveness()
        print("\n✅ Framework effectiveness measurement completed successfully!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error measuring framework effectiveness: {e}")
        sys.exit(1)
