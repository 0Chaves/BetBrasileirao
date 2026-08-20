<script setup>
defineProps({
  label: { type: String, required: true }, // "Casa", "Empate", "Visitante"
  selected: { type: Boolean, default: false },
  disabled: { type: Boolean, default: false }
})
defineEmits(['select'])
</script>

<template>
  <button
    type="button"
    :disabled="disabled"
    class="rounded-lg py-sm px-xs flex items-center justify-center transition-colors border disabled:opacity-40 disabled:cursor-not-allowed"
    :class="
      selected
        ? 'bg-secondary text-on-secondary border-secondary'
        : 'bg-surface-variant text-on-surface border-transparent hover:border-primary hover:bg-primary/20'
    "
    @click="$emit('select')"
  >
    <span class="font-label-sm text-label-sm" :class="selected ? 'text-on-secondary' : 'text-on-surface-variant'">
      {{ label }}
    </span>
  </button>
</template>
