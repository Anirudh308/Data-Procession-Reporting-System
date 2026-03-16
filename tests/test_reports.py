import os
import json
import pytest
from reporting.report_generator import ReportGenerator
from core.exceptions import ReportGenerationError

@pytest.fixture
def sample_stats():
    return {
        "age": {
            "column": "age",
            "count": 5,
            "mean": 30.0,
            "median": 28.0,
            "min": 22.0,
            "max": 45.0,
            "sum": 150.0,
            "std_dev": 8.5
        },
        "salary": {
            "column": "salary",
            "count": 5,
            "mean": 60000.0,
            "median": 55000.0,
            "min": 45000.0,
            "max": 80000.0,
            "sum": 300000.0,
            "std_dev": 12000.0
        }
    }

@pytest.fixture
def temp_output_dir(tmp_path):
    return str(tmp_path / "test_output")

def test_report_generator_init(temp_output_dir):
    generator = ReportGenerator(output_dir=temp_output_dir)
    assert os.path.exists(temp_output_dir)
    assert generator.output_dir == temp_output_dir

def test_generate_text_report(temp_output_dir, sample_stats):
    generator = ReportGenerator(output_dir=temp_output_dir)
    file_path = generator.generate_text_report(sample_stats, filename="test_report.txt")
    
    assert os.path.exists(file_path)
    with open(file_path, "r") as f:
        content = f.read()
        assert "DPRS DATA PROCESSING SYSTEM REPORT" in content
        assert "AGE" in content
        assert "SALARY" in content
        assert "30.0" in content
        assert "60000.0" in content

def test_generate_json_report(temp_output_dir, sample_stats):
    generator = ReportGenerator(output_dir=temp_output_dir)
    file_path = generator.generate_json_report(sample_stats, filename="test_export.json")
    
    assert os.path.exists(file_path)
    with open(file_path, "r") as f:
        data = json.load(f)
        assert data == sample_stats
        assert data["age"]["mean"] == 30.0
        assert data["salary"]["max"] == 80000.0

def test_report_generation_error(sample_stats):
    # Test directory creation failure
    # Using a path that is highly likely to fail creation
    invalid_dir = "/root/invalid/dir/that/does/not/exist" if os.name == 'posix' else "Z:\\invalid\\dir:*"
    
    with pytest.raises(ReportGenerationError):
        ReportGenerator(output_dir=invalid_dir)
