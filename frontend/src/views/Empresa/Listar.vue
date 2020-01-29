<template>
  <div class="container">
    <div class="col-md-12 card">
      <div class="header">
        <h2>Empresa</h2>
        <ul class="header-dropdown" style="top:10px;">
          <li class="dropdown">
            <router-link :to="{ name: 'crear_empresa' }" class="btn btn-info">
              Crear
            </router-link>
          </li>
        </ul>
      </div>
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
              NIT
            </th>
            <th scope="col">
              Dirección
            </th>
            <th scope="col">
              Telefono
            </th>
            <th scope="col">
              Correo
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
              <label class="" for="empresa">
                {{ emp.EMP_NIT_Empresa }}
              </label>
            </td>
            <td>
              <label class="" for="empresa">
                {{ emp.EMP_Direccion_Empresa }}
              </label>
            </td>
            <td>
              <label class="" for="empresa">
                {{ emp.EMP_Telefono_Empresa }}
              </label>
            </td>
            <td>
              <label class="" for="empresa">
                {{ emp.EMP_Correo_Empresa }}
              </label>
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
      loadingEmpresas: false
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
    }
  },
  created() {
    this.getEmpresas();
  }
};
</script>

<style>
.b {
  padding: 6px 12px;
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
