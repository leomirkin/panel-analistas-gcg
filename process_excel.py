import pandas as pd
import json
from datetime import datetime

def process_excel():
    try:
        # Leer el archivo Excel
        df = pd.read_excel('distribucion.xlsx')
        
        # Asumiendo que las columnas son: Cliente, Horario, Analista, WhatsApp, Interno
        df.columns = ['client', 'schedule', 'analyst', 'whatsapp', 'extension']
        
        # Diccionario para almacenar los datos de los analistas
        analysts_data = {}
        
        # Procesar cada fila del Excel
        for _, row in df.iterrows():
            analyst = row['analyst']
            # Dividir los clientes si hay varios (separados por coma)
            clients = [client.strip() for client in str(row['client']).split(',')]
            
            if analyst not in analysts_data:
                analysts_data[analyst] = {
                    'name': analyst,
                    'schedule': row['schedule'],
                    'clients': clients,
                    'extension': str(row['extension']),  # Usar el interno del Excel
                    'whatsapp': str(row['whatsapp']).strip()  # Agregar número de WhatsApp
                }
            else:
                # Agregar nuevos clientes a la lista existente
                analysts_data[analyst]['clients'].extend(clients)
                
        # Eliminar duplicados de clientes para cada analista
        for analyst in analysts_data:
            analysts_data[analyst]['clients'] = list(dict.fromkeys(analysts_data[analyst]['clients']))
            # Asegurarse de que el interno sea un string y manejar valores NaN
            if pd.isna(analysts_data[analyst]['extension']):
                analysts_data[analyst]['extension'] = "0000"
            else:
                analysts_data[analyst]['extension'] = str(int(float(analysts_data[analyst]['extension'])))
        
        # Convertir el diccionario a lista
        analysts_list = list(analysts_data.values())
        
        # Guardar los datos en un archivo JSON
        with open('analysts_data.json', 'w', encoding='utf-8') as f:
            json.dump(analysts_list, f, ensure_ascii=False, indent=4)
            
        print("Datos procesados exitosamente")
        return True
        
    except Exception as e:
        print(f"Error al procesar el Excel: {str(e)}")
        return False

if __name__ == "__main__":
    process_excel() 