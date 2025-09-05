import React, { useState, useEffect } from "react";

function ListarBeneficiarios() {
  const [beneficiarios, setBeneficiarios] = useState([]);

  useEffect(() => {
    // Simulación de datos que vendrían de una API
    const dataSimulada = [
      {
        idResultadoPostulacion: 1,
        resPostulacion: 101,
        resValoracion: 90,
        resResultado: 1, // 1 = Aprobado
        resFechaUpdate: "2025-08-10",
      },
      {
        idResultadoPostulacion: 2,
        resPostulacion: 102,
        resValoracion: 70,
        resResultado: 0, // 0 = No aprobado
        resFechaUpdate: "2025-08-15",
      },
      {
        idResultadoPostulacion: 3,
        resPostulacion: 103,
        resValoracion: 85,
        resResultado: 1,
        resFechaUpdate: "2025-08-20",
      },
    ];

    // Filtrar solo aprobados como beneficiarios
    setBeneficiarios(dataSimulada.filter(b => b.resResultado === 1));
  }, []);

  return (
    <div className="container">
      <h2>Listar Beneficiarios</h2>
      {beneficiarios.length > 0 ? (
        <table border="1" cellPadding="10" style={{ marginTop: "15px", width: "100%", textAlign: "center" }}>
          <thead>
            <tr>
              <th>ID Resultado</th>
              <th>ID Postulación</th>
              <th>Valoración</th>
              <th>Resultado</th>
              <th>Fecha de Actualización</th>
            </tr>
          </thead>
          <tbody>
            {beneficiarios.map((b) => (
              <tr key={b.idResultadoPostulacion}>
                <td>{b.idResultadoPostulacion}</td>
                <td>{b.resPostulacion}</td>
                <td>{b.resValoracion}</td>
                <td>{b.resResultado === 1 ? "Aprobado" : "No aprobado"}</td>
                <td>{b.resFechaUpdate}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No hay beneficiarios registrados.</p>
      )}
    </div>
  );
}

export default ListarBeneficiarios;
