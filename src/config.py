import os

PROJECT_DIR = os.getcwd()
RAW_DATA_DIR = os.path.join(PROJECT_DIR, 'data', 'raw')

# Renomeia as colunas de acordo com a documentação
COLUMN_NAMES = [
    'checking_account_status',
    'duration_in_month',
    'credit_history',
    'purpose',
    'credit_amount',
    'savings_account_bonds',
    'present_employment_since',
    'installment_rate_percent',
    'personal_status_and_sex',
    'other_debtors_guarantors',
    'present_residence_since',
    'property',
    'age_in_years',
    'other_installment_plans',
    'housing',
    'number_of_existing_credits',
    'job',
    'number_of_dependents',
    'telephone',
    'foreign_worker',
    'risk'
]