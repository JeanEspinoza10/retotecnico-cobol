import pandas as pd
import argparse
import os

class Reporte:
    def __init__(self, path_to_file):
        self.df = self.load_data(path_to_file)
        self.print_init()
    
    def print_init(self):
        '''
        Function for print part initial of reports.
        '''
        print(f"\nReporte de Transacciones\n{'-' * 45}\n")
        
    def load_data(self, path_to_file):
        '''
        Load data from CSV file.
        '''
        try:
            df = pd.read_csv(path_to_file)
            return df
        except Exception as e:
            raise Exception(f"Error in load_data: {e}")
            
    def get_final_balance(self):
        '''
        Get final balance of transactions for report.
        '''
        try:
            total_credit = 0
            total_debit = 0
            # Iterate over rows of dataframe
            for index, row in self.df.iterrows():
                if row["tipo"] == "Crédito":
                    total_credit += row["monto"]
                elif row["tipo"] == "Débito":
                    total_debit += row["monto"]
            balance_final = total_credit - total_debit
            print("Balance Final:", balance_final, "\n")
        except Exception as e:
           print("Error in get_final_balance: ", e)
            
    def get_high_amount_transactions(self):
        '''
        Get high amount transactions for report.
        '''
        try:
            value_high = 0
            id_high = 0
            # Iterate over rows of dataframe
            for index, row in self.df.iterrows():
                if row["monto"] > value_high:
                    value_high = row["monto"]
                    id_high = row["id"]
            print(f"Transacción de Mayor Monto: ID {id_high} - {value_high}","\n")
        except Exception as e:
            print("Error in get_high_amount_transactions: ", e)
    
    def get_transaction_count(self):    
        '''
        Get transaction count for report.
        '''
        try:
            unique_types = self.df["tipo"].unique()
            count_type = {element: 0 for element in unique_types}
            # Iterate over rows of dataframe
            for index, row in self.df.iterrows():
                if row["tipo"] in count_type:
                    count_type[row["tipo"]] += 1
            template = "Conteo de Transacciones:"
            for key, value in count_type.items():
                template += f" {key}: {value}"
            print(template,"\n")
        except Exception as e:
            print("Error in get_transaction_count: ", e)
            
if __name__ == "__main__":
    
    try:
        # Get the path to the file
        parser = argparse.ArgumentParser(description="Report of Transactions")
        parser.add_argument('--route', type=str, help="Route to the file")
        args = parser.parse_args()
        route_to_file = args.route
        
        # Generate the report
        reporte = Reporte(route_to_file)
        reporte.get_final_balance()
        reporte.get_high_amount_transactions()
        reporte.get_transaction_count()
  
    except Exception as e:
        print("Error in main: ", e)
  