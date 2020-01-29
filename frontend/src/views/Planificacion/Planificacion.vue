<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Lista de Contenidos</h2>
        </div>
        <div class=" body table-responsive">
          <form>
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
                      <option value="">
                        --Seleccione un tipo de campaña--
                      </option>
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
                      <option selected value="">
                        --Seleccione un Status--
                      </option>
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
            <div class="my-4">
              <p v-show="loadingComportamientos">...Cargando...</p>
              <button
                v-show="nextComportamiento"
                @click="getComportamientos('MAS')"
                class="btn btn-sm btn-outline-success"
              >
                Cargar Más
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </section>
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
