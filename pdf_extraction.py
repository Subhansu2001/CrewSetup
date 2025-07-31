from crewai import Agent, Task, Crew
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

class PDFExtractionCrew:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        
    def load_pdf(self):
        """Load PDF document using PyPDFLoader"""
        loader = PyPDFLoader(self.pdf_path)
        return loader.load()
    
    def create_agents(self):
        """Create specialized agents for PDF processing"""
        
        # Agent for extracting and organizing content
        extractor = Agent(
            role='PDF Content Extractor',
            goal='Extract and organize content from PDF documents efficiently',
            backstory='Expert at parsing and extracting information from PDF documents',
            allow_delegation=False
        )
        
        # Agent for analyzing and summarizing content
        analyzer = Agent(
            role='Content Analyzer',
            goal='Analyze and summarize extracted PDF content',
            backstory='Specialized in understanding and summarizing document content',
            allow_delegation=False
        )
        
        return extractor, analyzer
    
    def create_tasks(self, pages, extractor, analyzer):
        """Create tasks for PDF processing"""
        
        # Task for content extraction
        extraction_task = Task(
            description=f'Extract all text content from the PDF document at {self.pdf_path}',
            agent=extractor
        )
        
        # Task for content analysis and summarization
        analysis_task = Task(
            description='Analyze the extracted content and provide a comprehensive summary',
            agent=analyzer
        )
        
        return [extraction_task, analysis_task]
    
    def process_pdf(self):
        """Main method to process the PDF"""
        try:
            # Load the PDF
            pages = self.load_pdf()
            
            # Create agents
            extractor, analyzer = self.create_agents()
            
            # Create tasks
            tasks = self.create_tasks(pages, extractor, analyzer)
            
            # Create and run the crew
            crew = Crew(
                agents=[extractor, analyzer],
                tasks=tasks,
                verbose=True
            )
            
            result = crew.kickoff()
            return result
            
        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your PDF path
    pdf_path = "sample.pdf"
    
    crew = PDFExtractionCrew(pdf_path)
    result = crew.process_pdf()
    
    if result:
        print("PDF Processing Results:")
        print(result)
