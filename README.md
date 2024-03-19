# TProPep-filter


### Module Overview:

1. **filter**: filter interactions with certain original_class_label, predicted_class_label, and prediction confidence value.

2. **add_organism**: This module is used to add organism names for receptors and peptides.

3. **filter_organism**: This module is used to filter interactions based on interested organism information to match specific organisms.

4. **get_pubmed_id**: Fetch PubMed IDs of papers that contain pairs of PDB IDs.

## Module Details

### 1. Filter Module

#### Functionality:
This module allows users to filter data in CSV files based on given criteria.

#### Parameters:
- `input_file`: Path to the input CSV file.
- `output_file`: Path to the output CSV file.
- `class_label`: Index of the class label column, default is 2nd column.
- `predict_label`: Index of the predict label column, default is 4th column.
- `confidence_column`: Index of the prediction confidence column, default is 3rd column.
- `encoding`: Encoding of the input CSV file, default is UTF-8. Optional: 'ISO-8859-1'.
- `confidence_filter`: Confidence filter. For example, filtering out rows with confidence greater than 0.99999, default is 0.

### 2. Add Organism Module

#### Functionality:
This module is used to add organism information to CSV files, including organisms for receptors and peptides.

#### Parameters:
- `input_file`: Path to the input CSV file.
- `output_file`: Path to the output CSV file, with two extra columns of organisms.

### 3. Filter Organism Module

#### Functionality:
This module is used to filter interactions based on interested organism information to match specific organisms.

#### Parameters:
- `input_file`: Path to the input CSV file.
- `output_file`: Path to the output CSV file.
- `species_1`: Species 1, default is "Homo sapiens".
- `species_2`: Species 2, default is "Homo sapiens".

### 4. Fetch Pubmed ID Module

#### Functionality:
This module is used to fetch published PubMed IDs that contain pairs of PDB IDs.

#### Parameters:
- `input_file`: Path to the input CSV file.
- `output_file`: Path to the output CSV file, with two extra columns of PubMed IDs.
  
## Usage Example

```bash
python main.py filter input.csv output.csv --class_label 2 --predict_label 4 --confidence_column 3 --confidence_filter 0.9
