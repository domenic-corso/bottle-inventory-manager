<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="/static/css/master.css">
        <title>Inventory</title>
    </head>
    <body>
        <div style="min-width: 250px; max-width: 500px;">
            <div class="chooser">
                <div class="chooser__name">Inventory</div>
                <div class="chooser__list">
                    % for category in categories:
                        <div class="chooser__item" data-category="{{category['category_id']}}">
                            {{category['name']}}
                            <div class="chooser__itemdesc">{{category['description']}}</div>
                        </div>
                    % end
                </div>
            </div>
            <button class="button u-pull-right">New Category</button>
        </div>
    </body>
</html>
