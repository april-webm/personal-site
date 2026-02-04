const { format } = require("date-fns");

module.exports = function(eleventyConfig) {
  // Custom date filter
  eleventyConfig.addFilter("readableDate", dateObj => {
    return format(new Date(dateObj), "MMM d, yyyy");
  });

  // Copy the `css` directory and `cursor.png` to the output
  eleventyConfig.addPassthroughCopy("_src/css");
  eleventyConfig.addPassthroughCopy("cursor.png");

  // Set custom directories for input, output, includes, and data
  return {
    dir: {
      input: "_src",
      includes: "_includes",
      output: "april-webm.nekoweb.org"
    },
    // Passthrough files and directories
    passthroughFileCopy: true,
  };
};