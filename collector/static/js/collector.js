/*
     ╔╦╗╔═╗  ╔═╗┌─┐┬  ┬  ┌─┐┌─┐┌┬┐┌─┐┬─┐
      ║║╠═╝  ║  │ ││  │  ├┤ │   │ │ │├┬┘
     ═╩╝╩    ╚═╝└─┘┴─┘┴─┘└─┘└─┘ ┴ └─┘┴└─
*/

class Collector{
    constructor(ac,op,sc){
        let me = this;
        me.heartbeat = 0;
        me.ac = ac
        me.op = op
        me.sc = sc
        me.init();
    }

    init(){
        let me = this;
        _.defer(function(){
            me.rebootLinks();
            me.prepareAjax();
            me.loadAjax();
            me.loadKeywords();
            //me.dice_initialize(document.body,400);


            me.setToggler('.mobile_form_toggler', 'collapsed', "#customizer");
            me.setToggler('.menu_right_toggler', 'collapsed', ".menuright");
            me.setToggler('.list_toggler', 'collapsed', ".list");
            me.setToggler('#menu_right_toggler', 'collapsed', ".menuright");
            me.setToggler('#listtoggler', 'collapsed', ".list");
            me.setToggler('.dicer_toggler', 'collapsed', ".dicer");
            me.setToggler('#dicer_toggler', 'collapsed', ".dicer");
        });
    }

    loadAjax() {
        let me = this;
        $.ajax({
            url: 'ajax/storyline/none/',
            success: function(answer) {
                $('.storyline').html(answer)
                $.ajax({
                    url: 'ajax/list/none/1/',
                    success: function(answer) {
                        $('.charlist').html(answer)
                        me.rebootLinks();

                    },
                });
            },
        });
    }

    prepareAjax() {
        let me = this;
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    let csrf_middlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
                    //console.log(csrf_middlewaretoken)
                    xhr.setRequestHeader('X-CSRFToken', csrf_middlewaretoken);
                }
            }
        });
    }

    runHeartbeat(x=5000){
        let me = this;
        clearTimeout(me.heartbeat);
        $.ajax({
            url: 'api/heartbeat/',
            success: function(answer) {
                $('#messenger_block').html(answer)
                me.heartbeat = setTimeout("co.runHeartbeat()", x);
            },
        });
    }

    keywordHandlerClick(event) {
        let me = this;
        let firstPoint = chart_keywords.getElementAtEvent(event)[0];
        if (firstPoint) {
            let label = chart_keywords.data.labels[firstPoint._index];
            let value = chart_keywords.data.datasets[firstPoint._datasetIndex].data[firstPoint._index];
            $('#customize').val(label);
            $('#menu_search').click();
        }
    }

    loadKeywords() {
        let me = this;
        $.ajax({
            url: 'api/keywords/',
            success: function(answer) {
                $('#keywords').html('')
                $('#keywords').append(answer.chart);
                me.rebootLinks();
            }
        });
    }

    setToggler(tag, klass, item) {
        let me = this;
        $(tag).off().on('click', function(event) {
            $(item).toggleClass(klass);
            me.rebootLinks();
        });
    }

    rebootLinks() {
        let me = this;
        me.sc.doConnect(me);
        me.op.doConnect(me);
        me.ac.prepareEvents(me);
        console.log('Reboot links')

        me.heartbeat = setTimeout("co.runHeartbeat()", 500);
        /* MENU SHORTCUTS */
        $('#current_storyline').off('change').on('change', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let slug = $('#current_storyline').val();
            console.log(slug);
            $.ajax({
                url: 'ajax/storyline/' + slug + '/',
                success: function(answer) {
                    $('.storyline').html(answer)
                    $.ajax({
                        url: 'ajax/list/none/1/',
                        success: function(answer) {
                            //$('.charlist').html(answer)
                            //me.rebootLinks();
                            window.location = '/';
                        },
                    });
                },
            });
        });
        $("#menu_popstats").off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $.ajax({
                url: 'api/popstats/',
                success: function(answer) {
                    $('.details').html('')
                    answer.charts.forEach(function(elem) {
                        $('.details').append(elem);
                    });
                    me.rebootLinks();
                },
            });
            me.rebootLinks();
        });
        $("#menu_recalc").off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $.ajax({
                url: 'api/recalc/',
                success: function(answer) {
                    me.runHeartbeat();
                    me.rebootLinks();
                },
                error: function(answer){
                    console.error("Ooops");
                    console.log(answer);
                    me.runHeartbeat();
                    me.rebootLinks();
                }
            });
        });
        $('#menu_jumpweb').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $.ajax({
                url: 'jumpweb/show',
                success: function(answer) {
                    $('.details').html(answer);
                    let tab = window.open(null,'graphics');
                    tab.document.write(answer)

                    me.prepareAjax();
                    me.rebootLinks();
//                    let html = "<!DOCTYPE html><html>yo</html>";
//                    //let spacecharts = window.open("data:text/html," + encodeURIComponent(html),"Spacecharts");
//                    let spacecharts = window.open("about:blank","spacecharts");
//                    spacecharts.focus();
                },
                error: function(answer) {
                    console.error('ooops... on show jumpweb...');
                }
            });
        });
        $('#menu_todo').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $.ajax({
                url: 'todo/show',
                success: function(answer) {
                    $('.charlist').html(answer)
                    me.prepareAjax();
                    me.rebootLinks();
                },
                error: function(answer) {
                    console.error('ooops... on show jumpweb...');
                }
            });
        });
        $('#menu_go').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();

            let formdata = $('.character_form').serialize();
            let id = $('.character_form input[name=id]').val();
            let rid = $('.character_form input[name=rid]').val();

            let tgt = $('.character_form').attr('form-target');

            $.ajax({
                url: tgt+'s/' + id + '/edit/',
                type: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: formdata,
                dataType: 'json',
                success: function(answer) {
                    $('li').find('div.avatar_link').removeClass('selected');
                    //$('li').find('div.avatar_link').find('#' + id + '.view_character').click();
                    me.rebootLinks();
                    me.prepareAjax();
                    me.loadKeywords();
                },
                error: function(answer) {
                    console.log(answer.responseText);
                },
            });
        });
        $('#menu_add_avatar').off().on('click', function(event) {
            event.preventDefault();
            let name = $("#customize").val();
            $("#customize").val("");
            name = name.split(" ").join("-");
            $.ajax({
                url: 'ajax/add/avatar/' + name + '/',
                success: function(answer) {
                    $('.details').html(answer.character)
                    me.rebootLinks();
                    me.prepareAjax();
                    me.loadKeywords();
                },
                error: function(answer) {
                    $('.details').html('oops, broken')
                    me.rebootLinks();
                },
            });
        });
        $("#menu_conf_details").off().on('click', function(event) {
            event.preventDefault();
            $.ajax({
                url: 'ajax/conf_details/',
                success: function(answer) {
                    $('.details').html(answer)
                    me.rebootLinks();
                },
            });
        });
        $("#menu_build_config_pdf").off().on('click', function(event) {
            event.preventDefault();
            $.ajax({
                url: 'ajax/build_config_pdf/',
            }).done(function(answer) {
                $('.details').html(answer.comment);
                me.rebootLinks();
            });
        });
        $("#menu_login").off().on('click', function(event) {
            event.preventDefault();
            $.ajax({
                type:"GET",
                url: '/ajax/login/',
                data: $('#login_form').serialize(),
                success: function(answer){
                    $('#login_block').html(answer);
                    me.rebootLinks();
                },
                error: function(answer) {
                    $('.details').html(answer);
                    me.rebootLinks();
                }
            });
        });
        $("#login_button").off().on('click', function(event) {
            event.preventDefault();
            console.log("Login post !!!")
            $.ajax({
                type:"POST",
                url: '/ajax/login/',
                data: $('#login_form').serialize(),
                success: function(answer){
                    $('.user_block').html(answer);
                    window.location = '/';
                },
                error: function(answer) {
                    $('.details').html(answer);
                    me.rebootLinks();
                }
            });
        });
        $("#menu_logout").off().on('click', function(event) {
            event.preventDefault();
            $.ajax({
                type:"POST",
                url: '/ajax/logout/',
                success: function(answer){
                    $('.user_block').html(answer);
                    window.location = '/';
                },
                error: function(answer) {
                    $('.user_block').html(answer);
                    me.rebootLinks();
                }
            });
        });

        $("#menu_profile").off().on('click', function(event) {
            event.preventDefault();
            $.ajax({
                type:"POST",
                url: '/ajax/profile/',
                success: function(answer){
                    $('.details').html(answer);
                    console.log('profile ok')
                    me.rebootLinks();
                },
                error: function(answer) {
                    console.log('Error!!!')
                    $('.details').html(answer);
                    me.rebootLinks();
                }
            });
        });


        $('#menu_build_pdf_rules').off().on('click', function(event) {
            event.preventDefault();
            $.ajax({
                url: 'ajax/build_pdf_rules/',
            }).done(function(answer) {
                $('.details').html(answer.comment);
                me.rebootLinks();
            });
        });
        $("#menu_seek").off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let key = $('#customize').val();
            $.ajax({
                url: 'ajax/view/by_rid/' + key + '/',
                success: function(answer) {
                    $('.details').html(answer.character);
                    $('.avatars').html("");
                    _.forEach(answer.links,function(e){
                        $('.avatars').append("<li id='"+e.rid + "'>" + e.data + "</li>");
                    })
                    me.prepareAjax();
                    me.rebootLinks();
                },
                error: function(answer) {
                    console.error('Seek error...');
                    console.error(answer.character);
                }
            });
        });
        $("#menu_search").off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let key = $('#customize').val();
            if (key == '') {
                key = 'none';
            }
            $.ajax({
                url: 'ajax/list/' + key + '/1/',
                success: function(answer) {
                    $('.charlist').html(answer);
                    me.prepareAjax();
                    me.rebootLinks();
                },
            });
        });
        $('.custom_glance').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $('#customize').val($(this).attr('id'));
            $('#search').click();
        });
        $('.character_link').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            $.ajax({
                url: 'ajax/recalc/character/' + $(this).attr('id') + '/',
                success: function(answer) {
                    $('.details').html(answer.character);
                    me.rebootLinks();
                    ac.reset(answer.id, "sheet_" + answer.id, "customizer");
                },
                error: function(answer) {
                    console.log('Recalc error...' + answer);
                }
            });
        });
        $('.character_name').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let mine = $(this).parents('div.avatar_link').find('div.character_info');
            $('div.avatar_link').find('div.character_info').addClass('hidden');
            $(mine).toggleClass('hidden');
            me.rebootLinks();
        });
        $('.recalc_avatar').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let dad = $(this).parents('li');
            let x = $(this).parents('div').attr("id").split("_")[1];
            let dad_id = $(dad).attr("id");
            //let that_id = $(this).attr('id').split("_")[0];
            $("li#" + dad_id + " .character_info").removeClass('hidden');
            $.ajax({
                url: 'ajax/recalc/avatar/' + x + '/',
                success: function(answer) {
                    $('.details').html(answer.character);
                    $('li#' + answer.rid).html(answer.link);
                    $('#customizer').html(answer.mobile_form);
                    ac.reset(x, "sheet_" + x, "customizer");
                    $("li#" + dad_id + " .character_name").click();
                    me.rebootLinks();
                    //update_messenger();
                },
                error: function(answer) {
                    console.log('Recalc error...' + answer);
                }
            });
        });
        $('.wa_export_character').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let dad = $(this).parents('li');
            let x = $(this).parents('div').attr("id").split("_")[1];
            let dad_id = $(dad).attr("id");
            //let that_id = $(this).attr('id').split("_")[0];
            $("li#" + dad_id + " .character_info").removeClass('hidden');
            $.ajax({
                url: 'ajax/wa_export/character/' + x + '/',
                success: function(answer) {
                    $('.details').html(answer.character);
                    me.rebootLinks();

                },
                error: function(answer) {
                    console.log('Recalc error...' + answer);
                }
            });
        });

        $('.toggle_public').off().on('click', function(event) {
            event.preventDefault();
            let dad = $(this).parents('li');
            let x = $(this).parents('div').attr("id").split("_")[1];
            let dad_id = $(dad).attr("id");
            $("li#" + dad_id + " .character_info").removeClass('hidden');
            $("li#" + dad_id + " .avatar_link").css('border-color', 'red');
            $.ajax({
                url: 'toggle/' + x + '/public',
                success: function(answer) {
                    console.log(answer)
                    $('li#' + dad_id).html(answer.avatar_link);
                    me.rebootLinks();
                },
                error: function(answer) {
                    console.warn('Error on toggle...');
                },
            });
        });
        $('.toggle_spotlight').off().on('click', function(event) {
            event.preventDefault();
            let dad = $(this).parents('li');
            let x = $(this).parents('div').attr("id").split("_")[1];
            let dad_id = $(dad).attr("id");
            $("li#" + dad_id + " .character_info").removeClass('hidden');
            $("li#" + dad_id + " .avatar_link").css('border-color', 'red');
            console.log(x);
            $.ajax({
                url: 'toggle/' + x + '/spotlight',
                success: function(answer) {
                    console.log(answer)
                    $('li#' + dad_id).html(answer.avatar_link);
                    me.rebootLinks();
                },
                error: function(answer) {
                    console.warn('Error on toggle...');
                },
            });
        });

        /* Other links */
        $('.nav').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let key = $('#customize').val();
            if (key == '') {
                key = 'none';
            }
            $.ajax({
                url: 'ajax/list/' + key + '/' + $(this).attr('page') + '/',
                success: function(answer) {
                    $('.charlist').html(answer)
                    me.rebootLinks();
                },
            });
        });
        $('.episode_cast').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let slug = $(this).attr('id');
            $('#customize').val(slug);
            $.ajax({
                url: 'ajax/list/' + slug + '/' + $(this).attr('page') + '/',
                success: function(answer) {
                    $('.charlist').html(answer)
                    me.rebootLinks();
                },
            });
        });
        $('.edit_character').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let dad = $(this).parents('li');
            let dad_id = $(dad).attr("id");
            let x = $(this).parents('div').attr("id").split("_")[1];
            console.log(x);
            //let that_id = $(this).attr('id').split("_")[0];
            $("li#" + dad_id + " .character_info").removeClass('hidden');
            $.ajax({
                url: 'characters/' + x + '/edit/',
                success: function(answer) {
                    $('.details').html(answer);
                    $('li#' + answer.rid).html(answer.link);
                    me.rebootLinks();
                    ac.reset(x, "sheet_" + x, "customizer");
                    $("li#" + dad_id + " .character_name").click();
                    //update_messenger();
                },
                error: function(answer) {
                    console.log('ooops... :(');
                    //update_messenger();
                }
            });
        });

        $('.edit_investigator').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let dad = $(this).parents('li');
            let dad_id = $(dad).attr("id");
            let x = $(this).parents('div').attr("id").split("_")[1];
            console.log(x);
            //let that_id = $(this).attr('id').split("_")[0];
            $("li#" + dad_id + " .character_info").removeClass('hidden');
            $.ajax({
                url: 'investigators/' + x + '/edit/',
                success: function(answer) {
                    $('.details').html(answer);
                    $('li#' + answer.rid).html(answer.link);
                    me.rebootLinks();
                    ac.reset(x, "sheet_" + x, "customizer");
                    $("li#" + dad_id + " .character_name").click();
                    //update_messenger();
                },
                error: function(answer) {
                    console.log('ooops... :(');
                    //update_messenger();
                }
            });
        });



        $('.roll_dice').off().on('keypress', function(event) {
            if (event.which == 13){
                event.preventDefault();
                event.stopPropagation();
                console.log("enter key pressed")
                let formula = $(this).val().toLowerCase().replace(" ","_").replace("+","x").replace("!","i")
                console.log(formula)
                $.ajax({
                    url: 'ajax/roll_dice/' + formula + '/',
                    success: function(answer) {
                        $('.rolls').html(answer.rolls);
                        $('.mods').html(answer.mods);
                        $('.total').html(answer.total);
                        me.rebootLinks();
                        //pdate_messenger();
                    },
                    error: function(answer) {
                        console.log('Broken dice... :(');
                        //update_messenger();
                    }
                });
            }
        });
        $('.dice_roll').off().on('click', function(event) {
            event.preventDefault();
            event.stopPropagation();
            let arr = $(this).attr("id").split("-")
            console.log(arr)
            $("#set").val("1d12+"+arr[1]);
            //$("#throw").fireEvent('mouseup');
            $t.raise_event($t.id('throw'), 'mouseup');
            me.rebootLinks();
        });
    }
}

