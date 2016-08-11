module.exports = function(grunt) {

    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),

        uncss: {
            dist: {
                files: {
                    'static/css/main.css' : ['templates/404.html']
                }
            }
        }

    });

    grunt.loadNpmTasks('grunt-uncss');

    grunt.registerTask('default', ['uncss']);

};
