import json
import os
from datetime import datetime
from utils.logger import logger 
from core.exceptions import ReportGenerationError 

class ReportGenerator:
    """
    Responsible for generating text and JSON reports from statistical summaries.
    """
    
    def __init__(self, output_dir="output"):
        """
        Initializes the generator and ensures the output directory exists.
        """
        self.output_dir = output_dir
        try:
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
                logger.info(f"Created output directory: {self.output_dir}")
        except Exception as e:
            logger.error(f"Failed to create output directory: {e}")
            raise ReportGenerationError(f"Directory creation failed: {e}")

    def generate_text_report(self, stats_summary, filename="report.txt"):
        """
        Generates a human-readable text report.
        """
        file_path = os.path.join(self.output_dir, filename)
        try:
            with open(file_path, "w") as f:
                f.write("==========================================\n")
                f.write("   DPRS DATA PROCESSING SYSTEM REPORT     \n")
                f.write("==========================================\n")
                f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for key, value in stats_summary.items():
                    f.write(f"{key.upper():<15}: {value}\n")
                
                f.write("\n==========================================\n")
            
            logger.info(f"Text report successfully generated at {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error generating text report: {e}")
            raise ReportGenerationError(f"Text report failed: {e}")

    def generate_json_report(self, stats_summary, filename="export.json"):
        """
        Exports the statistical summary as a structured JSON file.
        """
        file_path = os.path.join(self.output_dir, filename)
        try:
            with open(file_path, "w") as f:
                json.dump(stats_summary, f, indent=4)
            
            logger.info(f"JSON export successfully generated at {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error generating JSON export: {e}")
            raise ReportGenerationError(f"JSON export failed: {e}")

    def display_summary_to_console(self, stats_summary):
        """
        Formats and prints the summary directly to the terminal.
        """
        print("\n--- Statistical Summary ---")
        for key, value in stats_summary.items():
            print(f"{key.capitalize()}: {value}")
        print("---------------------------\n")
        logger.info("Displayed summary to console.")