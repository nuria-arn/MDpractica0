class ConexionJDBC:

    def __init__(self):
        self.url = "jdbc:mysql://localhost:3306/IBEX35"
        self.propiedades = {
            "driver": "com.mysql.cj.jdbc.Driver",
            "user": "root",
            "password": "****"
        }

    def guardar_dataframe(self, data_frame, tabla, modo="overwrite"):
        data_frame.write.jdbc(url=self.url, table=tabla, mode=modo, properties=self.propiedades)