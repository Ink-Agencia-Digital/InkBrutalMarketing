<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Crear Empresa</h2>
        </div>
        <div class="body">
          <form @submit.prevent="onSubmit">
            <br />
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="empresa">Nombre Empresa</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="EMP_Nombre_Empresa"
                  placeholder="Nombre Empresa"
                  maxlength="100"
                />
              </div>
              <div class="form-group col-md-4">
                <label for="nit">NIT</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="EMP_NIT_Empresa"
                  placeholder="NIT Empresa"
                  maxlength="100"
                />
              </div>
              <div class="form-group col-md-4">
                <label for="direccion">Dirección</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="EMP_Direccion_Empresa"
                  placeholder="Dirección Empresa"
                  maxlength="100"
                />
              </div>
            </div>
            <div class="form-row">
              <div class="form-group col-md-4">
                <label for="telefono">Telefono</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="EMP_Telefono_Empresa"
                  placeholder="Telefono Empresa"
                  maxlength="100"
                />
              </div>
              <div class="form-group col-md-4">
                <label for="correo">Correo</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="EMP_Correo_Empresa"
                  placeholder="Correo Empresa"
                  maxlength="100"
                />
              </div>
              <div class="form-group col-md-4">
                <label for="correo">Cantidad Trabajadores</label>
                <select
                  id="tipo"
                  class="form-control"
                  v-model="EMP_Tamano_Empresa"
                  required
                >
                  <option selected disabled value="">
                    --Seleccione los trabajadores que operan en la empresa--
                  </option>
                  <option value="1 - 50">1 - 50</option>
                  <option value="1 - 50">51 - 200</option>
                  <option value="1 - 50">> 200</option>
                </select>
              </div>
            </div>
            <p v-if="error" class="muted mt-2" style="color: red;">
              {{ error }}
            </p>
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
    </div>
  </section>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      EMP_Tamano_Empresa: "",
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (!this.EMP_Nombre_Empresa) {
        this.error = "Por favor digite un nombre de la empresa";
      } else if (!this.EMP_NIT_Empresa) {
        this.error = "Por favor digite el NIT de la empresa";
      } else if (!this.EMP_Direccion_Empresa) {
        this.error = "Por favor digite la dirección de la empresa";
      } else if (!this.EMP_Telefono_Empresa) {
        this.error = "Por favor digite el telefono de la empresa";
      } else if (!this.EMP_Correo_Empresa) {
        this.error = "Por favor digite el correo de la empresa";
      } else if (!this.EMP_Tamano_Empresa) {
        this.error = "Por favor seleccione el tamaño de la empresa";
      } else if (this.EMP_Nombre_Empresa.length > 100) {
        this.error =
          "El nombre de la empresa no puede ser superior a 100 caracteres";
      } else if (this.EMP_NIT_Empresa.length > 30) {
        this.error =
          "El NIT de la empresa no puede ser superior a 30 caracteres";
      } else if (this.EMP_Direccion_Empresa.length > 100) {
        this.error =
          "La dirección de la empresa no puede ser superior a 100 caracteres";
      } else if (this.EMP_Telefono_Empresa.length > 30) {
        this.error =
          "El telefono de la empresa no puede ser superior a 30 caracteres";
      } else if (this.EMP_Correo_Empresa.length > 100) {
        this.error =
          "El correo de la empresa no puede ser superior a 100 caracteres";
      } else {
        let endpoint = "/api/empresa/";
        let method = "POST";
        apiService(endpoint, method, {
          EMP_Nombre_Empresa: this.EMP_Nombre_Empresa,
          EMP_NIT_Empresa: this.EMP_NIT_Empresa,
          EMP_Direccion_Empresa: this.EMP_Direccion_Empresa,
          EMP_Telefono_Empresa: this.EMP_Telefono_Empresa,
          EMP_Correo_Empresa: this.EMP_Correo_Empresa,
          EMP_Tamano_Empresa: this.EMP_Tamano_Empresa
        }).then(() => {
          this.$router.push({
            name: "listar_empresa"
          });
        });
      }
    }
  }
};
</script>

<style>
.background {
  position: absolute;
  z-index: 1;
  width: 98%;
  height: 169%;
  padding-top: 0%;
  padding-left: 0%;
  padding-right: 0%;
}
</style>
