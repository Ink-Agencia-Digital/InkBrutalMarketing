<template>
  <div class="container">
    <div class="col-md-8">
      <br /><br />
      <h1>Empresa</h1>
      <br />
      <router-link :to="{ name: 'empresa' }" class="b btn-info">
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
              <router-link :to="{ name: 'empresa' }" class="bp btn-primary">
                Modificar
              </router-link>
              <button type="button" class="bpn btn-danger">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <br />
      <h1>Persona</h1>
      <br />
      <router-link :to="{ name: 'persona' }" class="b btn-info">
        Crear
      </router-link>
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
              <router-link :to="{ name: 'persona' }" class="bp btn-primary">
                Modificar
              </router-link>
              <button type="button" class="bpn btn-danger">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      empresas: [],
      personas: []
    };
  },
  methods: {
    getEmpresas() {
      let endpoint = "/api/empresa/";
      apiService(endpoint).then(data => {
        this.empresas.push(...data.results);
      });
    },
    getPersonas() {
      let endpoint = "/api/persona/";
      apiService(endpoint).then(data => {
        this.personas.push(...data.results);
      });
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
