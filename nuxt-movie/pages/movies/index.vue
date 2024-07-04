<template>
  <div class="container px-2">
    <div class="title">
      <h2>Movies</h2>
    </div>
    <div class="content">
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum vero
        fugit illum eius atque unde non, molestiae iure delectus repudiandae ea
        saepe tempora ipsa, aliquid amet id quo deserunt natus?
      </p>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: "main",
})


</script>

<style scoped>
.container {
  z-index: 0;
  position: relative;
  width: 100vw;
  padding: 70px 0 0 0;
}
.content{
  overflow: hidden;
  margin-top: 70px;
}
.title {
  padding-top: 20px;
  position: fixed;
  z-index: 2;
  width: 100vw;
  height: fit-content;
  background: #141414;
}
</style>