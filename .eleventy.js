const { format } = require("date-fns");

module.exports = function(eleventyConfig) {
  // Custom date filters
  eleventyConfig.addFilter("readableDate", dateObj => {
    return format(new Date(dateObj), "MMM d, yyyy");
  });

  eleventyConfig.addFilter("htmlDateString", dateObj => {
    return format(new Date(dateObj), "yyyy-MM-dd");
  });

  // Absolute URL filter for sitemap
  eleventyConfig.addFilter("absoluteUrl", (url, base) => {
    try {
      return new URL(url, base).toString();
    } catch (e) {
      console.error("absoluteUrl filter error:", e);
      return url;
    }
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
    // Use Nunjucks for markdown files
    markdownTemplateEngine: "njk",
  };
};