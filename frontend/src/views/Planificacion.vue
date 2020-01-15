<template>
  <div class="container-fluid">
    <br /><br />
    <h1 class="titulo">Planificación de emails</h1>
    <br />
    <form>
      <br />
      <table class="table">
        <thead>
          <tr>
            <th scope="col">
              #
            </th>
            <th scope="col">
              Nombre de la Campaña
            </th>
            <th scope="col">
              Tipo de campaña
            </th>
            <th scope="col">
              Fecha de envío
            </th>
            <th scope="col">
              Frecuencia
            </th>
            <th scope="col">
              Horario(s)
            </th>
            <th scope="col">
              Segmentación
            </th>
            <th scope="col">
              Status
            </th>
            <th scope="col">
              Link del texto email
            </th>
            <th scope="col">
              Contenido
            </th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">
              1
            </th>
            <td>
              <input
                type="text"
                class="form-control"
                id="nombre"
                placeholder="Nombre de la campaña"
              />
            </td>
            <td>
              <select name="tipo" id="tipo" class="form-control">
                <option value="">--Seleccione un tipo de campaña--</option>
                <option
                  v-for="tc in tipoCampanas"
                  :key="tc.TCM_Id_Tipo_Campana"
                  :value="tc.TCM_Id_Tipo_Campana"
                >
                  {{ tc.TCM_Nombre_Tipo_Campana }}
                </option>
              </select>
            </td>
            <td>
              <input
                type="date"
                class="form-control"
                id="fecha"
                placeholder="Fecha de envío"
              />
            </td>
            <td>
              <input
                type="text"
                class="form-control"
                id="frecuencia"
                placeholder="Frecuencia"
              />
            </td>
            <td>
              <input
                type="time"
                class="form-control"
                id="hora"
                placeholder="Horario"
              />
            </td>
            <td>
              <input
                type="text"
                class="form-control"
                id="segmentacion"
                placeholder="Segmentacion"
              />
            </td>
            <td>
              <select id="status" class="form-control">
                <option selected value="">--Seleccione un Status--</option>
                <option 
                  v-for="est in estados"
                  :key="est.EST_Id_Estado"
                  :value="est.EST_Id_Estado"
                >
                  {{ est.EST_Nombre_Estado }}
                </option>
              </select>
            </td>
            <td>
              <input
                type="text"
                class="form-control"
                id="link"
                placeholder="Link del texto"
              />
            </td>
            <td>
              <select id="idea" class="form-control">
                <option selected>Contenido</option>
              </select>
            </td>
          </tr>
        </tbody>
      </table>
      <br />
      <button
        type="submit"
        class="btn btn-dark"
        style="background-color: #344675;"
      >
        Guardar
      </button>
    </form>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      tipoCampanas: [],
      estados: []
    };
  },
  methods: {
    getTipoCampanas() {
      let endpoint = "/api/tipo-campana/";
      apiService(endpoint).then(data => {
        this.tipoCampanas.push(...data.results);
      });
    },
    getEstados() {
      let endpoint = "/api/estado/";
      apiService(endpoint).then(data => {
        this.estados.push(...data.results);
      });
    }
  },
  created() {
    this.getTipoCampanas();
    this.getEstados();
  }
};
</script>
