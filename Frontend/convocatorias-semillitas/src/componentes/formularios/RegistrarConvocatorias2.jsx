import { useState } from "react";

function RegistrarConvocatorias({ convocatorias, onPostular }) {
  const [formData, setFormData] = useState({
    convocatoria: "",
    fechaHora: "",
    identificacion: "",
    correo: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (
      !formData.convocatoria ||
      !formData.identificacion ||
      !formData.correo
    ) {
      alert("Por favor completa los campos obligatorios");
      return;
    }

    onPostular(formData);

    setFormData({
      convocatoria: "",
      fechaHora: "",
      identificacion: "",
      correo: "",
    });
  };

  return (
    <form onSubmit={handleSubmit} className="p-3 border rounded bg-light mx-auto w-50">
  <h2 className="h4 mb-3">Postulación a convocatoria</h2>

  <label className="form-label">Convocatoria</label>
  <select
    name="convocatoria"
    value={formData.convocatoria}
    onChange={handleChange}
    className="form-select mb-3"
    required
  >
    <option value="">Selecciona una convocatoria</option>
    {convocatorias.map((c, i) => (
      <option key={i} value={c.nombre}>
        {c.nombre}
      </option>
    ))}
  </select>

  <label className="form-label">Fecha y hora de postulación</label>
  <input
    type="datetime-local"
    name="fechaHora"
    value={formData.fechaHora}
    onChange={handleChange}
    className="form-control mb-3"
    required
  />

  <label className="form-label">Identificación del aprendiz</label>
  <input
    type="text"
    name="identificacion"
    value={formData.identificacion}
    onChange={handleChange}
    placeholder="Número de documento"
    className="form-control mb-3"
    required
  />

  <label className="form-label">Correo electrónico</label>
  <input
    type="email"
    name="correo"
    value={formData.correo}
    onChange={handleChange}
    placeholder="ejemplo@correo.com"
    className="form-control mb-3"
    required
  />

  <button type="submit" className="btn btn-success w-100">
    Postularse
  </button>
</form>
  );
}

export default RegistrarConvocatorias;
