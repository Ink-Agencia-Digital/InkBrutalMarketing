<template>
  <section class="content">
    <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
      <div class="card">
        <div class="header">
          <h2>Empresas</h2>
          <ul class="header-dropdown" style="top:10px;">
            <li class="dropdown">
              <router-link :to="{ name: 'crear_empresa' }" class="btn btn-info">
                <i class="material-icons" style="color:white;">add</i>Crear
              </router-link>
            </li>
          </ul>
        </div>
        <div class="body">
          <p v-if="error" class="muted mt-2" style="color: red;">{{ error }}</p>
          <div class="table-responsive">
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
                <tr v-for="(emp, index) in empresas" :key="emp.EMP_Id_Empresa">
                  <th scope="row">
                    {{ ++index }}
                  </th>
                  <td>
                    {{ emp.EMP_Nombre_Empresa }}
                  </td>
                  <td>
                    {{ emp.EMP_NIT_Empresa }}
                  </td>
                  <td>
                    {{ emp.EMP_Direccion_Empresa }}
                  </td>
                  <td>
                    {{ emp.EMP_Telefono_Empresa }}
                  </td>
                  <td>
                    {{ emp.EMP_Correo_Empresa }}
                  </td>
                  <td>
                    <router-link
                      :to="{
                        name: 'editar_empresa',
                        params: { id: emp.EMP_Id_Empresa }
                      }"
                      title="Editar este Registro"
                    >
                      <i
                        class="material-icons text-info"
                        style="font-size: 20px;"
                      >
                        edit
                      </i>
                    </router-link>
                    <button
                      type="button"
                      class="btn-accion-tabla"
                      title="Eliminar este Registro"
                      @click="deleteEmpresa(emp.EMP_Id_Empresa)"
                    >
                      <i
                        class="material-icons text-danger"
                        style="font-size: 20px;"
                      >
                        delete
                      </i>
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
      </div>
    </div>
  </section>
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
