<template>
  <div class="container">
    <div class="col-md-8">
      <form @submit.prevent="onSubmit">
        <br /><br />
        <h1>Persona</h1>
        <br />
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="nombre">Nombres</label>
            <input
              type="text"
              class="form-control"
              v-model="PSN_Nombres_Persona"
              placeholder="Nombres"
              id="nombre"
              maxlength="45"
            />
          </div>
          <div class="form-group col-md-6">
            <label for="apellido">Apellidos</label>
            <input
              type="text"
              class="form-control"
              v-model="PSN_Apellidos_Persona"
              placeholder="Apellidos"
              id="nombre"
              maxlength="45"
            />
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="edad">Edad</label>
            <input
              type="text"
              class="form-control"
              v-model="PSN_Edad_Persona"
              placeholder="Edad"
              id="edad"
              maxlength="3"
            />
          </div>
          <div class="form-group col-md-6">
            <label for="sexo">Sexo</label>
            <select id="sexo" class="form-control" v-model="PSN_Sexo_Persona">
              <option selected value="">--Selecciona un Sexo--</option>
              <option value="Femenino">Femenino</option>
              <option value="Masculino">Masculino</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group col-md-6">
            <label for="escolaridad">Escolaridad</label>
            <select
              id="escolaridad"
              class="form-control"
              v-model="PSN_Escoladidad_Persona"
            >
              <option value="">--Seleccione una escolaridad--</option>
              <option
                v-for="esc in escolaridades"
                :key="esc.ESC_Id_Escolaridad"
                :value="esc.ESC_Id_Escolaridad"
              >
                {{ esc.ESC_Nombre_Escolaridad }}
              </option>
            </select>
          </div>
          <div class="form-group col-md-6">
            <label for="cargo">Cargo</label>
            <input
              type="text"
              class="form-control"
              v-model="PSN_Cargo_Persona"
              placeholder="Cargo"
              id="cargo"
              maxlength="45"
            />
          </div>
        </div>
        <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
        <br />
        <button
          type="submit"
          class="btn btn-dark"
          style="background-color: #344675;"
        >
          Guardar
        </button>
        <br /><br /><br />
      </form>
    </div>
  </div>
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
    apellidoAnterior: {
      type: String,
      required: true
    },
    edadAnterior: {
      type: String,
      required: true
    },
    sexoAnterior: {
      type: String,
      required: true
    },
    cargoAnterior: {
      type: String,
      required: true
    },
    escolaridadAnterior: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      escolaridades: [],
      PSN_Nombres_Persona: this.nombreAnterior,
      PSN_Apellidos_Persona: this.apellidoAnterior,
      PSN_Edad_Persona: this.edadAnterior,
      PSN_Sexo_Persona: this.sexoAnterior,
      PSN_Escoladidad_Persona: this.cargoAnterior,
      PSN_Cargo_Persona: this.escolaridadAnterior,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (!this.PSN_Nombres_Persona) {
        this.error = "Por favor digite los nombres";
      } else if (!this.PSN_Apellidos_Persona) {
        this.error = "Por favor digite los apellidos";
      } else if (!this.PSN_Edad_Persona) {
        this.error = "Por favor digite la edad";
      } else if (!this.PSN_Sexo_Persona) {
        this.error = "Por favor seleccione el sexo";
      } else if (!this.PSN_Escoladidad_Persona) {
        this.error = "Por favor seleccione la escolaridad";
      } else if (!this.PSN_Cargo_Persona) {
        this.error = "Por favor digite el cargo";
      } else if (this.PSN_Nombres_Persona.length > 45) {
        this.error = "El nombre no puede ser superior a 45 caracteres";
      } else if (this.PSN_Apellidos_Persona.length > 45) {
        this.error = "El apellido no puede ser superior a 45 caracteres";
      } else if (this.PSN_Edad_Persona.length > 3) {
        this.error = "La edad no puede ser superior a 45 caracteres";
      } else if (this.PSN_Cargo_Persona.length > 45) {
        this.error = "El cargo no puede ser superior a 45 caracteres";
      } else {
        let endpoint = `/api/persona/${this.id}/`;
        let method = "PUT";
        apiService(endpoint, method, {
          PSN_Nombres_Persona: this.PSN_Nombres_Persona,
          PSN_Apellidos_Persona: this.PSN_Apellidos_Persona,
          PSN_Edad_Persona: this.PSN_Edad_Persona,
          PSN_Sexo_Persona: this.PSN_Sexo_Persona,
          PSN_Escoladidad_Persona: this.PSN_Escoladidad_Persona,
          PSN_Cargo_Persona: this.PSN_Cargo_Persona
        }).then(() => {
          this.$router.push({
            name: "listar_empresa"
          });
        });
      }
    },
    getEscolaridades() {
      let endpoint = "/api/escolaridad/";
      apiService(endpoint).then(data => {
        this.escolaridades.push(...data.results);
      });
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/persona/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.nombreAnterior = data.PSN_Nombres_Persona;
    to.params.apellidoAnterior = data.PSN_Apellidos_Persona;
    to.params.edadAnterior = data.PSN_Edad_Persona;
    to.params.sexoAnterior = data.PSN_Sexo_Persona;
    to.params.cargoAnterior = data.PSN_Escoladidad_Persona;
    to.params.escolaridadAnterior = data.PSN_Cargo_Persona;
    return next();
  },
  created() {
    this.getEscolaridades();
  }
};
</script>

<style>
.dang {
  padding: 4% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
</style>
