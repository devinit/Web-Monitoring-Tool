const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
// const LiveReloadPlugin = require('webpack-livereload-plugin');

module.exports = {
  mode: "development",
  entry: ["@babel/polyfill", "./monitor/src/index.js"],
  output: {
    path: path.resolve(__dirname, "monitor/static/js/"),
    filename: "js/bundle.js",
    chunkFilename: "js/[name].bundle.js",
    publicPath: "/static/monitor/"
  },
  resolve: {
    extensions: [".js"]
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: "babel-loader"
      },
      {
        test: /\.(c|sc)ss$/,
        use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
      }
    ]
  },
  devtool: "eval-source-map",
  watch: true,
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/bundle.css"
    }),
    // new LiveReloadPlugin()
  ]
};
