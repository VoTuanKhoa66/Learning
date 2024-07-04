<template>
  <client-only>
    <vue-plyr :options="options">
      <div data-plyr-provider="youtube" :data-plyr-embed-id="id_movie"></div>
    </vue-plyr>
  </client-only>
</template>
  
<script setup>
import "plyr/dist/plyr.css";
import VuePlyr from "vue-plyr";
import { defineProps } from "vue";


const props = defineProps(["id_movie"]);

const options = {
    autoplay: true,
    youtube: {
      quality: 'highres', // Specify the desired quality ('small', 'medium', 'large', 'hd720', 'hd1080', 'highres')
    },
};
</script>
  
<style scoped>
</style>
  