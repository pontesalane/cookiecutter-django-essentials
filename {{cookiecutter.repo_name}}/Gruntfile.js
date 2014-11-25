module.exports = function (grunt) {

  var appConfig = grunt.file.readJSON('package.json');

  // Load grunt tasks automatically
  // see: https://github.com/sindresorhus/load-grunt-tasks
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take. Can help when optimizing build times
  // see: https://npmjs.org/package/time-grunt
  require('time-grunt')(grunt);

  var mozjpeg = require('imagemin-mozjpeg');

  var pathsConfig = function (appName) {
    this.app = appName || appConfig.name;

    return {
      app: this.app,
      templates: this.app + '/templates',
      css: this.app + '/static/css',
      sass: this.app + '/src/sass',
      fonts: this.app + '/static/fonts',
      images: this.app + '/src/img',
      images_otim: this.app + '/static/img',
      js: this.app + '/src/js',
      js_min: this.app + '/static/js',
      manageScript: this.app + '/manage.py'
    };
  };

  grunt.initConfig({

    paths: pathsConfig(),
    pkg: appConfig,

    // see: https://github.com/gruntjs/grunt-contrib-watch
    watch: {
      gruntfile: {
        files: ['Gruntfile.js']
      },
      compass: {
        files: ['<%= paths.sass %>/**/*.{scss,sass}'],
        tasks: ['compass:server']
      },
      livereload: {
        files: [
          '<%= paths.js %>/**/*.js',
          '<%= paths.sass %>/**/*.{scss,sass}',
          '<%= paths.app %>/**/*.html'
          ],
        options: {
          spawn: false,
          livereload: true,
        },
      },
      files: ['<%= paths.js %>/src/**/*.js'],
      tasks: ['newer:uglify:dev'],
    },

    // see: https://github.com/gruntjs/grunt-contrib-compass
    compass: {
      options: {
          sassDir: '<%= paths.sass %>',
          cssDir: '<%= paths.css %>',
          fontsDir: '<%= paths.fonts %>',
          imagesDir: '<%= paths.images_otim %>',
          relativeAssets: false,
          assetCacheBuster: false,
          raw: 'Sass::Script::Number.precision = 10\n',
          require: [
            'bourbon',
            'breakpoint',
          ]
      },
      dist: {
        options: {
          environment: 'production'
        }
      },
      server: {
        options: {
          // debugInfo: true
        }
      }
    },

    // see: https://github.com/gruntjs/grunt-contrib-uglify
    uglify: {
      dist: {
        options: {
          banner: '/* Minified for production. */'
        },
        files: {
          '<%= paths.js_min %>/project.min.js': ['<%= paths.js %>/**/*.js']
        }
      },
      dev: {
        options: {
          sourceMap: true,
          sourceMapName: '<%= paths.js %>/sourcemap.map',
          mangle: false,
          beautify: {
            beautify: true,
            bracketize: true,
            indent_level: 2,
            width: 80,
          },
        },
        files: {
          '<%= paths.js_min %>/project.min.js': ['<%= paths.js %>/**/*.js']
        }
      }
    },

    imagemin: {
      dist: {
        options: {
          optimizationLevel: 5,
          use: [mozjpeg()]
        },
        files: [{
          expand: true,
          cwd: '<%= paths.images %>',
          src: ['**/*.{png,jpg,gif}'],
          dest: '<%= paths.app %>/static/img/'
        }]
      }
    },

    // see: https://npmjs.org/package/grunt-bg-shell
    bgShell: {
      _defaults: {
        bg: true
      },
      runDjango: {
        cmd: 'python <%= paths.manageScript %> runserver 0.0.0.0:8080'
      }
    }
  });

  grunt.registerTask('serve', [
    'bgShell:runDjango',
    'newer:uglify:dev',
    'newer:imagemin:dist',
    'watch',
  ]);

  grunt.registerTask('build', [
    'compass:dist',
    'newer:uglify:dist',
    'newer:imagemin:dist'
  ]);

  grunt.registerTask('default', [
    'build'
  ]);
};
