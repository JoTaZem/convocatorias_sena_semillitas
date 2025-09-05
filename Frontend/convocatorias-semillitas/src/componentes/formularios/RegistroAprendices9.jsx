import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

export default function RegistroUsuarios() {
  const [formData, setFormData] = useState({
    nombres: "",
    apellidos: "",
    correo: "",
    username: "",
    password: "",
    rol: "",
    identificacion: "",
    ficha: "",
    programa: "",
    cargo: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Datos del registro:", formData);
    // Aquí iría la llamada al backend con fetch o axios
  };

  return (
    <div className="d-flex align-items-center justify-content-center vh-100 bg-light">
      <div className="card shadow-lg p-4" style={{ width: "28rem" }}>
        <h2 className="text-center mb-4">Registro de Usuario</h2>
        <form onSubmit={handleSubmit}>
          {/* Nombre */}
          <div className="mb-3">
            <label className="form-label">Nombres</label>
            <input
              type="text"
              name="nombres"
              value={formData.nombres}
              onChange={handleChange}
              className="form-control"
              required
            />
          </div>

          {/* Apellidos */}
          <div className="mb-3">
            <label className="form-label">Apellidos</label>
            <input
              type="text"
              name="apellidos"
              value={formData.apellidos}
              onChange={handleChange}
              className="form-control"
              required
            />
          </div>

          {/* Correo */}
          <div className="mb-3">
            <label className="form-label">Correo</label>
            <input
              type="email"
              name="correo"
              value={formData.correo}
              onChange={handleChange}
              className="form-control"
              required
            />
          </div>

          {/* Usuario */}
          <div className="mb-3">
            <label className="form-label">Usuario</label>
            <input
              type="text"
              name="username"
              value={formData.username}
              onChange={handleChange}
              className="form-control"
              required
            />
          </div>

          {/* Contraseña */}
          <div className="mb-3">
            <label className="form-label">Contraseña</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              className="form-control"
              required
            />
          </div>

          {/* Rol */}
          <div className="mb-3">
            <label className="form-label">Rol</label>
            <select
              name="rol"
              value={formData.rol}
              onChange={handleChange}
              className="form-select"
              required
            >
              <option value="">Seleccione un rol</option>
              <option value="LIDER">Líder</option>
              <option value="FUNCIONARIO">Funcionario</option>
              <option value="APRENDIZ">Aprendiz</option>
            </select>
          </div>

          {/* Campos adicionales por Rol */}
          {formData.rol === "APRENDIZ" && (
            <>
              <div className="mb-3">
                <label className="form-label">Identificación</label>
                <input
                  type="text"
                  name="identificacion"
                  value={formData.identificacion}
                  onChange={handleChange}
                  className="form-control"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label">Ficha</label>
                <input
                  type="text"
                  name="ficha"
                  value={formData.ficha}
                  onChange={handleChange}
                  className="form-control"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label">Programa</label>
                <input
                  type="text"
                  name="programa"
                  value={formData.programa}
                  onChange={handleChange}
                  className="form-control"
                  required
                />
              </div>
            </>
          )}

          {formData.rol === "FUNCIONARIO" && (
            <div className="mb-3">
              <label className="form-label">Cargo</label>
              <input
                type="text"
                name="cargo"
                value={formData.cargo}
                onChange={handleChange}
                className="form-control"
                required
              />
            </div>
          )}

          {/* Botón */}
          <button type="submit" className="btn btn-primary w-100">
            Registrar
          </button>
        </form>
      </div>
    </div>
  );
}
