<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Lista de Contenidos</h2>
        </div>
        <div class=" body table-responsive">
          <div class="form-group">
            <h3>Persona</h3>
            <select id="persona" class="form-control" required>
              <option selected value="">--Seleccione una persona--</option>
              <option
                v-for="psn in personas"
                :key="psn.PSN_Id_Persona"
                :value="psn.PSN_Id_Persona"
              >
                {{ psn.PSN_Nombres_Persona }} {{ psn.PSN_Apellidos_Persona }}
              </option>
            </select>
          </div>
          <form>
            <br />
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">
                    #
                  </th>
                  <th scope="col">
                    Idea
                  </th>
                  <th scope="col">
                    Formato
                  </th>
                  <th scope="col">
                    Etapa de compra
                  </th>
                  <th scope="col">
                    Persona Foco
                  </th>
                  <th scope="col">
                    Relevancia
                  </th>
                  <th scope="col">
                    Status
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">
                    1
                  </th>
                  <td>
                    <label class="" for="idea">Idea</label>
                  </td>
                  <td>
                    <select id="formato" class="form-control" required>
                      <option selected value="">
                        --Seleccione un formato--
                      </option>
                      <option
                        v-for="fmt in formatos"
                        :key="fmt.FMT_Id_Formato"
                        :value="fmt.FMT_Id_Formato"
                      >
                        {{ fmt.FMT_Nombre_Formato }}
                      </option>
                    </select>
                  </td>
                  <td>
                    <select id="etapa" class="form-control">
                      <option selected>--Seleccione una etapa--</option>
                      <option
                        v-for="etp in etapas"
                        :key="etp.ETP_Id_Etapa"
                        :value="etp.ETP_Id_Etapa"
                      >
                        {{ etp.ETP_Descripcion_Etapa }}
                      </option>
                    </select>
                  </td>
                  <td>
                    <select id="persona" class="form-control">
                      <option selected>--Seleccione una persona--</option>
                      <option
                        v-for="psn in personas"
                        :key="psn.PSN_Id_Persona"
                        :value="psn.PSN_Id_Persona"
                      >
                        {{ psn.PSN_Nombres_Persona }}
                        {{ psn.PSN_Apellidos_Persona }}
                      </option>
                    </select>
                  </td>
                  <td>
                    <select id="relevancia" class="form-control">
                      <option selected>--Seleccione una relevancia--</option>
                      <option value="1">Alta</option>
                      <option value="2">Media</option>
                      <option value="3">Baja</option>
                    </select>
                  </td>
                  <td>
                    <select id="status" class="form-control">
                      <option selected>--Seleccione un estado--</option>
                      <option
                        v-for="est in estados"
                        :key="est.EST_Id_Estado"
                        :value="est.EST_Id_Estado"
                      >
                        {{ est.EST_Nombre_Estado }}
                      </option>
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
      personas: [],
      ideas: [],
      formatos: [],
      etapas: [],
      estados: []
    };
  },
  methods: {
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    getIdeas() {
      let endpoint = "/api/idea/";
      apiService(endpoint).then(data => {
        this.ideas.push(...data.results);
      });
    },
    getFormatos() {
      let endpoint = "/api/formato/";
      apiService(endpoint).then(data => {
        this.formatos.push(...data.results);
      });
    },
    getEtapas() {
      let endpoint = "/api/etapa/";
      apiService(endpoint).then(data => {
        this.etapas.push(...data.results);
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
    this.getPersonas();
    this.getIdeas();
    this.getFormatos();
    this.getEtapas();
    this.getEstados();
  }
};
</script>
