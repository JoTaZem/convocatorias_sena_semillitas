import React from "react";

function ListarPostulados() {
  // Datos de prueba (puedes reemplazar con datos de tu backend)
  const postulados = [
    {
      idPostulacion: 1,
      posConvocatoria: "Convocatoria 2025-01",
      posAprendiz: "Juan Pérez",
      posFechaHoraPostulacion: "2025-08-29 10:30:00",
    },
    {
      idPostulacion: 2,
      posConvocatoria: "Convocatoria 2025-01",
      posAprendiz: "María Gómez",
      posFechaHoraPostulacion: "2025-08-29 11:15:00",
    },
  ];

  return (
    <div className="container">
      <h2> Listar Postulados</h2>
      <table className="postulados-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Convocatoria</th>
            <th>Aprendiz</th>
            <th>Fecha de Postulación</th>
          </tr>
        </thead>
        <tbody>
          {postulados.map((postulado) => (
            <tr key={postulado.idPostulacion}>
              <td>{postulado.idPostulacion}</td>
              <td>{postulado.posConvocatoria}</td>
              <td>{postulado.posAprendiz}</td>
              <td>{postulado.posFechaHoraPostulacion}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Un poco de estilo en CSS */}
      <style jsx>{`
        .container {
          margin: 20px;
          padding: 20px;
          background: #f9f9f9;
          border-radius: 10px;
          box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        h2 {
          color: #333;
          margin-bottom: 15px;
        }
        .postulados-table {
          width: 100%;
          border-collapse: collapse;
        }
        .postulados-table th,
        .postulados-table td {
          border: 1px solid #ddd;
          padding: 10px;
          text-align: left;
        }
        .postulados-table th {
          background-color: #007bff;
          color: white;
        }
        .postulados-table tr:nth-child(even) {
          background-color: #f2f2f2;
        }
        .postulados-table tr:hover {
          background-color: #e6f7ff;
        }
      `}</style>
    </div>
  );
}

export default ListarPostulados;
