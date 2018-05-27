SELECT "chat_app_chat"."id", "chat_app_chat"."user_id", "chat_app_chat"."message", "chat_app_chat"."date",
to_tsvector(COALESCE("chat_app_chat"."message", ))
AS "search", ts_rank(to_tsvector(COALESCE("chat_app_chat"."message", )), plainto_tsquery(inno))
AS "rank" FROM "chat_app_chat"
WHERE UPPER(to_tsvector(COALESCE("chat_app_chat"."message", ))::text)
LIKE UPPER(%inno%) ORDER BY "rank" DESC

SELECT school, city
FROM schools
WHERE to_tsvector('english'::regconfig, COALESCE(school, '') || ' ' || COALESCE(city, ''))
    @@ (plainto_tsquery('english'::regconfig, 'alamo')) = true;

SELECT school, city
FROM schools
WHERE (school_city_idx @@ (to_tsquery('mission & viej:*')) = true);

# working query
Chat.objects.extra(where=["to_tsvector(coalesce(message, '')) @@ (to_tsquery('inn:*')) = true"]).values('message')