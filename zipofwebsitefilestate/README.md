# April's Personal Website

This website is built using the [Eleventy](https://www.11ty.dev/) static site generator.

## Getting Started

### 1. Install Dependencies

Before you begin, make sure you have [Node.js](https://nodejs.org/) installed on your machine.

Then, open your terminal in the project root and run the following command to install the necessary dependencies:

```bash
npm install
```

### 2. Running the Development Server

To start the local development server, run the following command:

```bash
npx @11ty/eleventy --serve
```

This will build the site and make it available at `http://localhost:8080/`. The server will automatically rebuild the site and reload your browser whenever you make changes to the source files in the `_src` directory.

### 3. Building for Production

When you are ready to deploy your site, run the following command:

```bash
npx @11ty/eleventy
```

This will generate the final, static website in the `april-webm.nekoweb.org` directory. You can then upload the contents of this directory to your Nekoweb hosting.

## How to Add a New Blog Post

Adding a new blog post is simple:

1.  Create a new Markdown file (e.g., `my-new-post.md`) in the `_src/posts` directory.
2.  At the top of the file, add the following "front matter":

    ```yaml
    ---
    layout: "post.njk"
    title: "Your Post Title"
    date: YYYY-MM-DD
    tags: ["post"]
    ---
    ```
    *   `layout`: Should always be `"post.njk"`.
    *   `title`: The title of your blog post.
    *   `date`: The date the post was published.
    *   `tags`: Must include `"post"` for it to appear in the blog list.

3.  Write your blog post content below the front matter using Markdown.
4.  Run the build command (`npx @11ty/eleventy`) to generate the new post.
