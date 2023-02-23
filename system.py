import pandas as pd
from datetime import date
a = date.today()

reg = {'id' : 1,
       'Nome': 'Pedro',
       'Livro': 'Lovecraft',
       'Data' : a}

reg_df = pd.DataFrame(reg)