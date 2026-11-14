-- Mis Ahorros: tabla para sincronizar entre teléfono y PC.
-- Cada usuario tiene una sola fila con sus datos, y solo él puede verla o cambiarla.

create table if not exists public.ahorros (
  user_id uuid primary key default auth.uid() references auth.users(id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.ahorros enable row level security;

drop policy if exists "ver mis datos" on public.ahorros;
drop policy if exists "crear mis datos" on public.ahorros;
drop policy if exists "cambiar mis datos" on public.ahorros;

create policy "ver mis datos" on public.ahorros
  for select to authenticated using ((select auth.uid()) = user_id);

create policy "crear mis datos" on public.ahorros
  for insert to authenticated with check ((select auth.uid()) = user_id);

create policy "cambiar mis datos" on public.ahorros
  for update to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

revoke all on public.ahorros from anon;
grant select, insert, update on public.ahorros to authenticated;
