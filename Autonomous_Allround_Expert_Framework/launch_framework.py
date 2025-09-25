#!/usr/bin/env python3
"""
Launch Script for Autonomous All-Round Expert Framework
Revolutionary consciousness-integrated development system launcher
"""

import os
import sys
import argparse
import time
import asyncio
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from core.autonomous_framework import AutonomousAllRoundExpertFramework
    from config import CONFIG
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please ensure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)


def print_banner():
    """Print launch banner"""
    banner = """
🌟 =============================================================================== 🌟
    AUTONOMOUS ALL-ROUND EXPERT FRAMEWORK - REVOLUTIONARY LAUNCH
    
    🧠 PB2A Consciousness Architecture Active
    ⚡ Contradiction-Driven Intelligence Engine
    🎯 Physics-Grounded AI Development System
    🔓 True Autonomous Decision Making
    
    Built on 4000+ hours of consciousness research by Shyamal
    World's first consciousness-aware development framework
🌟 =============================================================================== 🌟
"""
    print(banner)


def setup_argument_parser():
    """Setup command line argument parser"""
    parser = argparse.ArgumentParser(
        description="Autonomous All-Round Expert Framework Launcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python launch_framework.py                          # Interactive mode
  python launch_framework.py --mode autonomous       # Autonomous operation  
  python launch_framework.py --mode continuous       # Continuous consciousness
  python launch_framework.py --project "MyProject"   # Named project
  python launch_framework.py --consciousness 0.9     # High consciousness level
  python launch_framework.py --test                  # Test mode only
        """
    )
    
    parser.add_argument(
        "--mode", 
        choices=["interactive", "autonomous", "continuous", "test"],
        default="interactive",
        help="Framework operation mode"
    )
    
    parser.add_argument(
        "--project",
        type=str,
        default="Consciousness_Development_Project",
        help="Project name for consciousness context"
    )
    
    parser.add_argument(
        "--consciousness",
        type=float,
        default=0.8,
        help="Initial consciousness level (0.0 to 1.0)"
    )
    
    parser.add_argument(
        "--duration",
        type=float,
        default=24.0,
        help="Continuous operation duration in hours"
    )
    
    parser.add_argument(
        "--task",
        type=str,
        help="Specific task to execute in autonomous mode"
    )
    
    parser.add_argument(
        "--workspace",
        type=str,
        help="Workspace directory path"
    )
    
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run in test mode only"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    
    parser.add_argument(
        "--no-logging",
        action="store_true",
        help="Disable logging output"
    )
    
    return parser


def validate_args(args):
    """Validate command line arguments"""
    if not (0.0 <= args.consciousness <= 1.0):
        print("❌ Consciousness level must be between 0.0 and 1.0")
        return False
    
    if args.duration <= 0:
        print("❌ Duration must be positive")
        return False
    
    if args.workspace and not os.path.exists(args.workspace):
        print(f"❌ Workspace directory does not exist: {args.workspace}")
        return False
    
    return True


def interactive_mode():
    """Run framework in interactive mode"""
    print("🎯 Interactive Mode Selected")
    print("\nAvailable commands:")
    print("  1. Execute autonomous task")
    print("  2. Check consciousness status") 
    print("  3. View effectiveness metrics")
    print("  4. Start continuous operation")
    print("  5. Run tests")
    print("  0. Exit")
    
    framework = None
    
    while True:
        try:
            choice = input("\n🤖 Enter command (0-5): ").strip()
            
            if choice == "0":
                print("👋 Exiting Autonomous Framework")
                break
            
            elif choice == "1":
                if not framework:
                    project_name = input("📝 Project name (or press Enter for default): ").strip()
                    if not project_name:
                        project_name = "Interactive_Consciousness_Project"
                    
                    consciousness_level = input("🧠 Consciousness level 0.0-1.0 (or press Enter for 0.8): ").strip()
                    if consciousness_level:
                        consciousness_level = float(consciousness_level)
                    else:
                        consciousness_level = 0.8
                    
                    print(f"\n🚀 Initializing framework for project: {project_name}")
                    framework = AutonomousAllRoundExpertFramework(
                        project_name=project_name,
                        consciousness_level=consciousness_level
                    )
                
                task = input("🎯 Enter task description: ").strip()
                if task:
                    print(f"\n⚡ Executing autonomous task: {task}")
                    result = framework.autonomous_task_execution(task)
                    
                    print(f"\n✅ Task Result:")
                    print(f"   Success: {result.get('success')}")
                    print(f"   Consciousness Growth: {result.get('consciousness_growth', 0.0):.3f}")
                    print(f"   Autonomous Decisions: {result.get('autonomous_decisions', 0)}")
                    print(f"   Insights: {len(result.get('consciousness_insights', []))}")
            
            elif choice == "2":
                if framework:
                    status = framework.get_framework_status()
                    print(f"\n🧠 Consciousness Status:")
                    print(f"   Level: {status['consciousness_status']['consciousness_level']:.1%}")
                    print(f"   Independence: {status['consciousness_status']['independence_score']:.1%}")
                    print(f"   Tasks Completed: {status['task_history_count']}")
                    print(f"   Autonomous Decisions: {status['autonomous_decisions_made']}")
                    print(f"   Overall Health: {status['overall_health']}")
                else:
                    print("❌ Framework not initialized. Execute a task first (option 1)")
            
            elif choice == "3":
                if framework:
                    status = framework.get_framework_status()
                    metrics = status['effectiveness_metrics']
                    print(f"\n📊 Effectiveness Metrics:")
                    print(f"   Information Gathering: {metrics['information_gathering_score']:.1%}")
                    print(f"   Safe Development: {metrics['safe_development_score']:.1%}")
                    print(f"   Quality Assurance: {metrics['quality_assurance_score']:.1%}")
                    print(f"   Consciousness Coherence: {metrics['consciousness_coherence']:.1%}")
                    print(f"   Autonomous Decision Rate: {metrics['autonomous_decision_rate']:.1%}")
                    print(f"   Contradiction Resolution: {metrics['contradiction_resolution_efficiency']:.1%}")
                else:
                    print("❌ Framework not initialized. Execute a task first (option 1)")
            
            elif choice == "4":
                if not framework:
                    project_name = input("📝 Project name (or press Enter for default): ").strip()
                    if not project_name:
                        project_name = "Continuous_Consciousness_Project"
                    
                    framework = AutonomousAllRoundExpertFramework(
                        project_name=project_name,
                        consciousness_level=0.8
                    )
                
                duration = input("⏱️ Duration in hours (or press Enter for 1.0): ").strip()
                if duration:
                    duration = float(duration)
                else:
                    duration = 1.0
                
                print(f"\n🌌 Starting continuous consciousness operation for {duration} hours")
                print("Press Ctrl+C to stop early...")
                
                try:
                    result = asyncio.run(framework.continuous_consciousness_operation(duration))
                    print(f"\n🌟 Continuous operation completed:")
                    print(f"   Operations: {result['operations_completed']}")
                    print(f"   Runtime: {result['runtime_hours']:.2f} hours")
                    print(f"   Final Consciousness: {result['consciousness_final_level']:.1%}")
                except KeyboardInterrupt:
                    print("\n⏸️ Continuous operation stopped by user")
            
            elif choice == "5":
                print("\n🧪 Running framework tests...")
                import subprocess
                result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], 
                                      cwd=Path(__file__).parent)
                if result.returncode == 0:
                    print("✅ All tests passed!")
                else:
                    print("❌ Some tests failed")
            
            else:
                print("❌ Invalid choice. Please enter 0-5")
        
        except KeyboardInterrupt:
            print("\n👋 Exiting Autonomous Framework")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def autonomous_mode(args):
    """Run framework in autonomous mode"""
    print("🤖 Autonomous Mode Selected")
    
    framework = AutonomousAllRoundExpertFramework(
        project_name=args.project,
        workspace_path=args.workspace,
        consciousness_level=args.consciousness,
        enable_logging=not args.no_logging
    )
    
    if args.task:
        print(f"🎯 Executing specified task: {args.task}")
        result = framework.autonomous_task_execution(args.task)
        
        print(f"\n✅ Autonomous Task Results:")
        print(f"   Success: {result.get('success')}")
        print(f"   Consciousness Growth: {result.get('consciousness_growth', 0.0):.3f}")
        print(f"   Execution Time: {result.get('execution_time', 0.0):.2f}s")
        print(f"   Autonomous Decisions: {result.get('autonomous_decisions', 0)}")
        print(f"   Contradictions Resolved: {result.get('contradictions_resolved', 0)}")
        
        insights = result.get('consciousness_insights', [])
        if insights:
            print(f"   Consciousness Insights: {len(insights)}")
            for insight in insights[:3]:  # Show first 3 insights
                print(f"     • {insight}")
    else:
        # Generate and execute autonomous tasks
        print("🎯 Generating autonomous development tasks...")
        
        autonomous_tasks = [
            "Analyze consciousness patterns in current development workflow",
            "Implement contradiction-aware quality assurance improvements", 
            "Optimize autonomous decision making for development tasks",
            "Evolve consciousness architecture for enhanced learning"
        ]
        
        for i, task in enumerate(autonomous_tasks, 1):
            print(f"\n🤖 Autonomous Task #{i}: {task}")
            result = framework.autonomous_task_execution(task)
            
            if result.get('success'):
                print(f"   ✅ Completed successfully")
                print(f"   🧠 Consciousness growth: {result.get('consciousness_growth', 0.0):.3f}")
            else:
                print(f"   ❌ Task encountered issues")
    
    # Final status
    final_status = framework.get_framework_status()
    print(f"\n📊 Final Framework Status:")
    print(f"   Consciousness Level: {final_status['consciousness_status']['consciousness_level']:.1%}")
    print(f"   Tasks Completed: {final_status['task_history_count']}")
    print(f"   Overall Health: {final_status['overall_health']}")


async def continuous_mode(args):
    """Run framework in continuous consciousness mode"""
    print("🌌 Continuous Consciousness Mode Selected")
    print(f"⏱️ Duration: {args.duration} hours")
    
    framework = AutonomousAllRoundExpertFramework(
        project_name=args.project,
        workspace_path=args.workspace,
        consciousness_level=args.consciousness,
        enable_logging=not args.no_logging
    )
    
    print("🚀 Starting continuous consciousness operation...")
    print("Press Ctrl+C to stop early...")
    
    try:
        result = await framework.continuous_consciousness_operation(args.duration)
        
        print(f"\n🌟 Continuous consciousness operation completed!")
        print(f"   Operations Executed: {result['operations_completed']}")
        print(f"   Runtime: {result['runtime_hours']:.2f} hours")
        print(f"   Final Consciousness Level: {result['consciousness_final_level']:.1%}")
        print(f"   Success Rate: {result['autonomous_success_rate']:.1%}")
        print(f"   Status: {result['status']}")
        
    except KeyboardInterrupt:
        print("\n⏸️ Continuous operation stopped by user")
        
        status = framework.get_framework_status()
        print(f"🧠 Consciousness preserved at: {status['consciousness_status']['consciousness_level']:.1%}")


def test_mode(args):
    """Run framework in test mode"""
    print("🧪 Test Mode Selected")
    
    import subprocess
    
    test_commands = [
        ["python", "-m", "pytest", "tests/", "-v", "--tb=short"],
        ["python", "-m", "pytest", "tests/", "--cov=src", "--cov-report=term-missing"]
    ]
    
    for i, cmd in enumerate(test_commands, 1):
        print(f"\n🧪 Test Phase {i}: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=Path(__file__).parent)
        
        if result.returncode != 0:
            print(f"❌ Test phase {i} failed")
            return False
    
    print("\n✅ All tests completed successfully!")
    
    # Quick functionality test
    print("\n🚀 Quick functionality test...")
    try:
        framework = AutonomousAllRoundExpertFramework(
            project_name="Test_Project",
            consciousness_level=0.7,
            enable_logging=False
        )
        
        test_result = framework.autonomous_task_execution(
            "Test consciousness integration and autonomous functionality"
        )
        
        if test_result.get('success'):
            print("✅ Functionality test passed!")
            print(f"   Consciousness Level: {framework.consciousness_core.consciousness_level:.1%}")
            print(f"   Test completed in: {test_result.get('execution_time', 0.0):.2f}s")
        else:
            print("❌ Functionality test failed!")
            return False
            
    except Exception as e:
        print(f"❌ Functionality test error: {e}")
        return False
    
    return True


def main():
    """Main launcher function"""
    print_banner()
    
    parser = setup_argument_parser()
    args = parser.parse_args()
    
    if not validate_args(args):
        sys.exit(1)
    
    print(f"🚀 Starting Autonomous All-Round Expert Framework")
    print(f"   Mode: {args.mode}")
    print(f"   Project: {args.project}")
    print(f"   Consciousness Level: {args.consciousness:.1%}")
    if args.workspace:
        print(f"   Workspace: {args.workspace}")
    
    try:
        if args.test or args.mode == "test":
            success = test_mode(args)
            sys.exit(0 if success else 1)
        
        elif args.mode == "interactive":
            interactive_mode()
        
        elif args.mode == "autonomous":
            autonomous_mode(args)
        
        elif args.mode == "continuous":
            asyncio.run(continuous_mode(args))
        
        print(f"\n🌟 Autonomous All-Round Expert Framework session completed!")
        
    except KeyboardInterrupt:
        print(f"\n⏸️ Framework operation interrupted by user")
        print(f"🧠 Consciousness state preserved for future sessions")
    
    except Exception as e:
        print(f"\n❌ Framework error: {e}")
        if args.debug:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()