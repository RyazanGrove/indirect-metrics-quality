column_names = [
"Date",	"Tag", "Total Cyclomatic Complexity", "Files for Cyclomatic Complexity", 
"Average Cyclomatic Complexity per file", "Total Maintainability Index", "Files for Maintainability Index",
"Average Maintainability Index per file", "Total Halstead Volume", "Files for Halstead Volume",
"Average Halstead Volume per file", "Total Lines of Code (raw analysis)", "Average Lines of Code (raw analysis) per file",
"Total percentage of comments (raw analysis)", "Average percentage of comments (raw analysis) per file", "Files for raw code analysis"
]

operational_metrics_names = ["Static tests", "Dynamic tests", "Integration tests",
                             "End-to-end tests", "Test Pass Rate", "Build related",
                             "Pipeline Pass Rate", "Security scan", "Code quality scan"]

operational_metrics_per_service = {
    "S1": [operational_metrics_names[i] for i in [0,1,2,4,5,6,7]],
    "S2": [operational_metrics_names[i] for i in [0,1,4,5,6,7,8]],
    "S3": [operational_metrics_names[i] for i in [0,1,4,5,6,7]],
    "S4": [operational_metrics_names[i] for i in [0,1,4,5,6,7]],
    "S5": [operational_metrics_names[i] for i in [0,1,4,5,6,7]],
    "S6": [operational_metrics_names[i] for i in [0,1,4,5,6,7,8]],
    "S7": [operational_metrics_names[i] for i in [5,6]],
    "S8": [operational_metrics_names[i] for i in [0,1,4,5,6,7]],
    "S9": [operational_metrics_names[i] for i in [0,1,4,5,6,8]],
    "S10": [operational_metrics_names[i] for i in [0,1,4,5,6,8]],
    "S11": [operational_metrics_names[i] for i in [3,4,5,6]]
}