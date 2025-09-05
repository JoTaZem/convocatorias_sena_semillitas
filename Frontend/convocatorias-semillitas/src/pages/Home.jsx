import React from "react";
//import PiePagina from "../componentes/PiePagina.jsx";

const Home = () => {
  return (
    <div className="d-flex flex-column min-vh-100 bg-light">
      {/* Encabezado */}
      <header className="bg-primary text-white text-center py-4 shadow-sm">
        <h1>🌱 Proyecto Convocatorias SENA</h1>
        <p className="mb-0">Gestión de convocatorias de bienestar para aprendices</p>
      </header>

      {/* Contenido principal */}
      <main className="container flex-grow-1 py-5">
        <div className="row g-4">
          <div className="col-md-4">
            <div className="card shadow-sm h-100">
              <div className="card-body text-center">
                <h5 className="card-title">👩‍🎓 Aprendices</h5>
                <p className="card-text">
                  Regístrate, postúlate y consulta los resultados de tus convocatorias.
                </p>
                <a href="/aprendiz" className="btn btn-primary">
                  Ir al módulo
                </a>
              </div>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card shadow-sm h-100">
              <div className="card-body text-center">
                <h5 className="card-title">👨‍💼 Funcionarios</h5>
                <p className="card-text">
                  Revisa información de postulantes y asigna evaluaciones.
                </p>
                <a href="/funcionario" className="btn btn-success">
                  Ir al módulo
                </a>
              </div>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card shadow-sm h-100">
              <div className="card-body text-center">
                <h5 className="card-title">👩‍💻 Líderes</h5>
                <p className="card-text">
                  Registra convocatorias, gestiona usuarios y genera reportes.
                </p>
                <a href="/lider" className="btn btn-warning">
                  Ir al módulo
                </a>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Pie de página */}
    </div>
  );
};

export default Home;
