<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Crear Persona</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link
                :to="{ name: 'listar_persona' }"
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
                <select
                  id="sexo"
                  class="form-control"
                  v-model="PSN_Sexo_Persona"
                >
                  <option disabled value="">
                    --Selecciona un Sexo--
                  </option>
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
                  <option value="" disabled>
                    --Seleccione una escolaridad--
                  </option>
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
            <p v-if="error" class="muted mt-2" style="color: red;">
              {{ error }}
            </p>
            <router-link :to="{ name: 'listar_persona' }" class="btn btn-danger"
              >Cancelar</router-link
            >
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
  data() {
    return {
      escolaridades: [],
      PSN_Sexo_Persona: "",
      PSN_Escoladidad_Persona: "",
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
        let endpoint = "/api/persona/";
        let method = "POST";
        apiService(endpoint, method, {
          PSN_Nombres_Persona: this.PSN_Nombres_Persona,
          PSN_Apellidos_Persona: this.PSN_Apellidos_Persona,
          PSN_Edad_Persona: this.PSN_Edad_Persona,
          PSN_Sexo_Persona: this.PSN_Sexo_Persona,
          PSN_Escoladidad_Persona: this.PSN_Escoladidad_Persona,
          PSN_Cargo_Persona: this.PSN_Cargo_Persona
        }).then(() => {
          this.$router.push({
            name: "listar_persona"
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
