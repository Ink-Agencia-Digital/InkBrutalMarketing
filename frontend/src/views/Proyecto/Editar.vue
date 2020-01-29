<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Editar Proyecto</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'listar_proyecto' }"
                class="btn btn-danger"
              >
                <i class="material-icons" style="font-size: 20px;">
                  keyboard_backspace
                </i>
                Volver
              </router-link>
            </li>
          </ul>
        </div>
        <div class="body">
          <form @submit.prevent="onSubmit">
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="proyecto">Nombre del proyecto</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="PRY_Nombre_Proyecto"
                  placeholder="Titulo Proyecto"
                  id="proyecto"
                  maxlength="150"
                />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="empresa">Empresa</label>
                <select
                  id="empresa"
                  class="form-control"
                  v-model="PRY_Empresa_Proyecto_id"
                >
                  <option disabled value="">
                    --Seleccione una Empresa--
                  </option>
                  <option
                    v-for="emp in empresas"
                    :key="emp.EMP_Id_Empresa"
                    :value="emp.EMP_Id_Empresa"
                  >
                    {{ emp.EMP_Nombre_Empresa }}
                  </option>
                </select>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-12">
                <label for="persona">Persona</label>
                <select
                  id="persona"
                  class="form-control"
                  v-model="PRY_Persona_Proyecto_id"
                >
                  <option selected disabled value="">
                    --Seleccione una Persona--
                  </option>
                  <option
                    v-for="psn in personas"
                    :key="psn.PSN_Id_Persona"
                    :value="psn.PSN_Id_Persona"
                  >
                    {{
                      psn.PSN_Nombres_Persona + " " + psn.PSN_Apellidos_Persona
                    }}
                  </option>
                </select>
              </div>
            </div>
            <p v-if="error" class="muted mt-2" style="color: red;">
              {{ error }}
            </p>
            <router-link
              :to="{ name: 'listar_proyecto' }"
              class="btn btn-danger"
            >
              Cancelar
            </router-link>
            &nbsp;
            <button
              type="submit"
              class="btn btn-dark"
              style="background-color: #344675;"
            >
              Guardar
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  props: {
    id: {
      type: Number,
      required: true
    },
    nombreAnterior: {
      type: String,
      required: true
    },
    empresaAnterior: {
      type: String,
      required: true
    },
    personaAnterior: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      empresas: [],
      personas: [],
      PRY_Nombre_Proyecto: this.nombreAnterior,
      PRY_Empresa_Proyecto_id: this.empresaAnterior,
      PRY_Persona_Proyecto_id: this.personaAnterior,
      error: null
    };
  },
  methods: {
    getEmpresas() {
      let endpoint = "/api/empresa/";
      this.empresas = [];
      apiService(endpoint).then(data => {
        this.empresas.push(...data.results);
      });
    },
    getPersonas() {
      let endpoint = "/api/persona/";
      this.personas = [];
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
    },
    onSubmit() {
      if (!this.PRY_Nombre_Proyecto) {
        this.error = "Por favor digite el titulo o nombre del proyecto";
      } else if (!this.PRY_Empresa_Proyecto_id) {
        this.error = "Por favor seleccione una empresa";
      } else if (!this.PRY_Persona_Proyecto_id) {
        this.error = "Por favor seleccione una persona";
      } else if (this.PRY_Nombre_Proyecto.length > 150) {
        this.error =
          "El titulo o nombre del proyecto nombre no puede ser superior a 45 caracteres";
      } else {
        let endpoint = `/api/proyecto/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, {
          PRY_Nombre_Proyecto: this.PRY_Nombre_Proyecto,
          PRY_Empresa_Proyecto: this.PRY_Empresa_Proyecto_id,
          PRY_Persona_Proyecto: this.PRY_Persona_Proyecto_id
        }).then(() => {
          this.$router.push({
            name: "listar_proyecto"
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/proyecto/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.nombreAnterior = data.PRY_Nombre_Proyecto;
    to.params.empresaAnterior = data.PRY_Empresa_Proyecto;
    to.params.personaAnterior = data.PRY_Persona_Proyecto;
    return next();
  },
  created() {
    this.getEmpresas();
    this.getPersonas();
  }
};
</script>
