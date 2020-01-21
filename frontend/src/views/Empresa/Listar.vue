<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Empresa</h1>
      <br />
      <router-link :to="{ name: 'crear_empresa' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
      <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
      <table class="table" id="tabla-data">
        <thead class="thead-dark">
          <tr>
            <th scope="col">
              #
            </th>
            <th scope="col">
              Empresa
            </th>
            <th scope="col">
              Nombre del proyecto
            </th>
            <th scope="col">
              Acción
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="emp in empresas" :key="emp.EMP_Id_Empresa">
            <th scope="row">
              {{ emp.EMP_Id_Empresa }}
            </th>
            <td>
              <label class="" for="empresa">
                {{ emp.EMP_Nombre_Empresa }}
              </label>
            </td>
            <td>
              <label class="" for="proyecto">Proyecto</label>
            </td>
            <td>
              <router-link
                :to="{
                  name: 'editar_empresa',
                  params: { id: emp.EMP_Id_Empresa }
                }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button
                type="button"
                class="bpn btn-danger"
                @click="deleteEmpresa(emp.EMP_Id_Empresa)"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="my-4">
        <p v-show="loadingEmpresas">...Cargando...</p>
        <button
          v-show="nextEmpresa"
          @click="getEmpresas('MAS')"
          class="btn btn-sm btn-outline-success"
        >
          Cargar Más
        </button>
      </div>
      <br />
      <h1>Persona</h1>
      <br />
      <router-link :to="{ name: 'crear_persona' }" class="b btn-info">
        Crear
      </router-link>
      <br /><br /><br />
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th scope="col">
              #
            </th>
            <th scope="col">
              Nombre
            </th>
            <th scope="col">
              Apellido
            </th>
            <th scope="col">
              Escolaridad
            </th>
            <th scope="col">
              Acción
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="psn in personas" :key="psn.PSN_Id_Persona">
            <th scope="row">
              {{ psn.PSN_Id_Persona }}
            </th>
            <td>
              <label class="" for="nombre">
                {{ psn.PSN_Nombres_Persona }}
              </label>
            </td>
            <td>
              <label class="" for="apellido">
                {{ psn.PSN_Apellidos_Persona }}
              </label>
            </td>
            <td>
              <label class="" for="escolaridad">
                {{ psn.PSN_Escoladidad_Persona.ESC_Nombre_Escolaridad }}
              </label>
            </td>
            <td>
              <router-link
                :to="{
                  name: 'editar_persona',
                  params: { id: psn.PSN_Id_Persona }
                }"
                class="bp btn-primary"
              >
                Modificar
              </router-link>
              <button
                type="button"
                class="bpn btn-danger"
                @click="deletePersona(psn.PSN_Id_Persona)"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="my-4">
        <p v-show="loadingPersonas">...Cargando...</p>
        <button
          v-show="nextPersona"
          @click="getPersonas('MAS')"
          class="btn btn-sm btn-outline-success"
        >
          Cargar Más
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      empresas: [],
      nextEmpresa: null,
      loadingEmpresas: false,
      personas: [],
      loadingPersonas: false,
      nextPersona: null
    };
  },
  methods: {
    getEmpresas(accion = null) {
      let endpoint = "/api/empresa/";
      if (accion == "DELETE") {
        this.empresas = [];
        apiService(endpoint).then(data => {
          this.empresas.push(...data.results);
        });
      } else {
        if (this.nextEmpresa) {
          endpoint = this.nextEmpresa;
        }
        this.loadingEmpresas = true;
        apiService(endpoint).then(data => {
          this.empresas.push(...data.results);
          this.loadingEmpresas = false;
          if (data.next) {
            this.nextEmpresa = data.next;
          } else {
            this.nextEmpresa = null;
          }
        });
      }
    },
    async deleteEmpresa(empresa) {
      let endpoint = `/api/empresa/${empresa}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getEmpresas("DELETE");
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    },
    getPersonas(accion = null) {
      let endpoint = "/api/persona-join/";
      if (accion == "DELETE") {
        this.personas = [];
        apiService(endpoint).then(data => {
          this.personas.push(...data.results);
        });
      } else {
        if (this.nextPersona) {
          endpoint = this.nextPersona;
        }
        this.loadingPersonas = true;
        apiService(endpoint).then(data => {
          this.personas.push(...data.results);
          this.loadingPersonas = false;
          if (data.next) {
            this.nextPersona = data.next;
          } else {
            this.nextPersona = null;
          }
        });
      }
    },
    async deletePersona(persona) {
      let endpoint = `/api/persona/${persona}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.getPersonas("DELETE");
      } catch (err) {
        this.error = "No es posible eliminar el registro";
      }
    }
  },
  created() {
    this.getEmpresas();
    this.getPersonas();
  }
};
</script>

<style>
.b {
  padding: 2% 3%;
  text-align: center;
  font-size: 16px;
  border-radius: 8px;
}
.bp {
  padding: 4% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
.bpn {
  padding: 2% 4%;
  text-align: center;
  font-size: 16px;
  border-radius: 6px;
}
</style>
