import xml.etree.ElementTree as ET
import csv

# Parse the XML file
xml_file = '/mnt/data/report.xml'  # Replace with the correct file path
tree = ET.parse(xml_file)
root = tree.getroot()

# Open a CSV file for writing
csv_file = 'output.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Metric ID', 'Metric Name', 'Avg', 'Max', 'Min', 'Number of Instances', 'Severity'])
    
    # Process the <Metrics> section
    metrics = root.find('Metrics')
    if metrics:
        for metric in metrics.findall('Metric'):
            metric_id = metric.get('id', 'N/A')
            metric_name = metric.get('name', 'N/A')
            avg = metric.get('avg', 'N/A')
            max_value = metric.get('max', 'N/A')
            min_value = metric.get('min', 'N/A')
            noi = metric.get('noi', 'N/A')
            sev = 'high' if float(avg) > 5 else 'low'  # Example logic for severity

            writer.writerow([metric_id, metric_name, avg, max_value, min_value, noi, sev])

print(f'CSV file "{csv_file}" created successfully.')
