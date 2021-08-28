module.exports = {
  purge: [
    '../templates/*.html',
    '../components/*.js',
    
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      background:"var(--background)",
      f_high:"var(--f_high)",
      f_med:"var(--f_med)",
      f_low:"var(--f_low)",
      f_inv:"var(--f_inv)",
      b_high:"var(--b_high)",
      b_med:"var(--b_med)",
      b_low:"var(--b_low)",
      b_inv:"var(--b_inv)",
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
