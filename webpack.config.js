const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
// const LiveReloadPlugin = require('webpack-livereload-plugin');

module.exports = {
  mode: 'development',
  entry: {
    monitor: ['@babel/polyfill', './monitor/src/index.jsx'],
  },
  output: {
    path: path.resolve(__dirname, ''),
    filename: '[name]/static/[name]/js/bundle.js',
    chunkFilename: '[name]/static/[name]/js/[name].bundle.js',
  },
  resolve: {
    extensions: ['.js'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
      {
        test: /\.scss$/,
        use: [MiniCssExtractPlugin.loader, 'sass-loader'],
      },
    ],
  },
  devtool: 'eval-source-map',
  watch: true,
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name]/static/[name]/css/bundle.css',
    }),
    // new LiveReloadPlugin()
  ],
};
