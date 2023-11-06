import pandas as pd

class MrClean():
    DEFINITIONS_ORDERED = [
        'id', 'grade', 'condition', 'floors', 'bedrooms', 'bathrooms', 
        'waterfront', 'year_built', 'year_renovated', 
        'selling_price', 'selling_date', 'view',
        'sqft_living','sqft_lot','sqft_above','sqft_basement',
        'sqft_living15','sqft_lot15',
        'zipcode', 'lat','lon'
    ]
    DEFINITIONS_DATATYPES = {
        'waterfront':     'bool',
        'view':           'int',
        'year_renovated': 'int',
        'year_built' :    'int',
        'bedrooms':       'int',
        'sqft_above':     'int',
        'sqft_basement':  'int',
        'sqft_living':    'int',
        'sqft_lot':       'int',
        'sqft_living15':  'int',
        'sqft_lot15':     'int',
    }
    DEFINITIONS_RENAME = {
        'date':         'selling_date', 
        'price':        'selling_price', 
        'long':         'lon',
        'yr_built':     'year_built',
        'yr_renovated': 'year_renovated'
    }

    def __init__(self, filepath):
        self.read_dataframe(filepath)

    def declutter(self):
        self.rename_columns()
        self.reorder_columns()
        self.fill_missing_all()
        self.fix_year_renovated()
        self.fix_selling_date()
        self.fix_dtypes()
        self.set_index_column('id')
        return self.df

    def read_dataframe(self, filepath):
        self.df = pd.read_csv(filepath)

    def rename_columns(self):
        self.df = self.df.rename(self.DEFINITIONS_RENAME, axis=1)

    def reorder_columns(self):
        self.df = self.df.reindex(self.DEFINITIONS_ORDERED, axis=1)

    def fill_missing_all(self):
        self.df.fillna(0, inplace=True)

    def fill_missing_col(self,column):
        self.df[column].fillna(0, inplace=True)

    def fix_year_renovated(self):
        self.df.year_renovated = self.df.year_renovated / 10

    def fix_selling_date(self, fn=pd.to_datetime):
        self.df.selling_date = fn(self.df.selling_date, format='%Y-%m-%d')

    def fix_dtypes(self):
        self.df = self.df.astype(self.DEFINITIONS_DATATYPES)

    def set_index_column(self, field='id'):
        self.df.set_index(field, inplace=True)

