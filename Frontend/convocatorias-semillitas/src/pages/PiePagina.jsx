import React from "react";

const PiePagina = () => {
  return (
    <footer className="bg-dark text-white text-center py-4 mt-auto">
      <div className="container">
        <p className="mb-1">
          © {new Date().getFullYear()} Proyecto Convocatorias SENA - CTPI Cauca
        </p>
        <div>
          <a href="/" className="text-white me-3 text-decoration-none">
            Inicio
          </a>
          <a href="/sobre" className="text-white me-3 text-decoration-none">
            Sobre Nosotros
          </a>
          <a href="/contacto" className="text-white text-decoration-none">
            Contacto
          </a>
        </div>
      </div>
    </footer>
  );
};

export default PiePagina;
