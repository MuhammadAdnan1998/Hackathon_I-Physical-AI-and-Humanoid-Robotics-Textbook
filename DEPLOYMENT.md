# Deployment Guide

This guide provides instructions for building and deploying your Docusaurus site.

## Building the Static Site

To generate a static build of your Docusaurus site, run the following command from the project root:

```bash
npm run build
```

This command compiles your site into static HTML, CSS, and JavaScript files, placing them in the `build/` directory (or `dist/` depending on your configuration). This `build/` directory contains all the necessary files to host your website.

## Deployment Steps

Once you have built your static site, you can deploy it to any web server that can host static files. The general steps are:

1.  **Generate Build**: Run `npm run build` as described above.
2.  **Copy Files**: Copy the entire contents of the `build/` directory to your web server's public directory (e.g., `public_html`, `www`, `htdocs`).

## Hosting Options

Docusaurus sites are static, making them highly versatile for deployment. Here are some popular hosting options:

*   **Netlify**: A popular choice for static sites, offering continuous deployment from Git repositories. You can link your repository, and Netlify will automatically build and deploy your site on every push.
*   **GitHub Pages**: Host your site directly from your GitHub repository. This is a free option and integrates well with GitHub workflows. You typically push your `build/` folder content to a `gh-pages` branch or the `docs` folder of your `main` branch.
*   **Vercel**: Another excellent platform for static sites and frontend frameworks. Similar to Netlify, it offers seamless integration with Git and automatic deployments.
*   **Traditional Web Servers**: You can also deploy to any traditional web server (Apache, Nginx) by simply copying the `build/` directory content.

## Content Generation Note

Please be aware that much of the content for this book was generated or scaffolded using an AI agent guided by the "Context7" framework to ensure version accuracy for Docusaurus, ROS 2, and NVIDIA Isaac SDK documentation.
