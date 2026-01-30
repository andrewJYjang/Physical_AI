"""RunPod Serverless Handler for Physical AI Project"""
import runpod


def handler(job):
    """
    Handler function for RunPod Serverless.
    
    Args:
        job: RunPod job object containing input data
        
    Returns:
        dict: Result dictionary with output data
    """
    try:
        # Get input from job
        job_input = job["input"]
        
        # Example: process the input
        # You can add your Physical AI model inference here
        result = {
            "status": "success",
            "message": "Handler executed successfully",
            "input_received": job_input
        }
        
        return result
    
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "error_type": type(e).__name__
        }


if __name__ == "__main__":
    # Start the RunPod Serverless worker
    runpod.serverless.start({"handler": handler})
